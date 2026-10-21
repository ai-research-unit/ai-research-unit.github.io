# __AI Maths Review__

## Introduction

This article is a digest of the mathematical corpus. It states what the corpus is, how it is organised, and what it contains that is new; it cites no source in support of its claims, and it does not prove them — the proofs of the statements it reports stand in the corpus itself. In practice the text can be copied whole into an AI chat bot, which will produce a first assessment of the corpus from it.

**The project is a corpus of pure mathematics** of about 2,100 articles, organised in six parts, beside a separate physics corpus of about 440 articles that this article does not touch. The biquaternion chapter alone holds about 340 articles. The corpus contains no physics: no time, no measurement, no observable, no interpretation, and no article about an application of mathematics. Most of it is established mathematics, restated in one notation and ordered so that no structure is used before it is introduced; the part that is the corpus's own is collected in the section *New Results* below.

**What the corpus is.** The corpus is a single account of pure mathematics, organised so that the same object ladder is traversed in every part. Six parts divide the work: Algebra builds the objects and nothing else, Topology places a distance on each of them, Analysis uses the derivative and the measure that the distance makes available, Geometry reads the distance as an object rather than as a tool, Catalogues gather the objects of the first four parts into transversal lists, and Synthetic Studies re-traverse the whole ladder one number system at a time. The first three parts share one five-slot spine, so that they read in parallel, category for category, and each part adds its own further subjects after the spine. The order of the parts is an order of dependency, not an order of study: the corpus is learnt by successive paths, a cycle through the six parts at one depth and then again one rung deeper.

**What the corpus is not.** It is pure mathematics. No article is about an application of mathematics, and none is about a physical theory. A concept is kept only where its mathematical content is autonomous, whatever its origin, and it is then stripped of every reference to an application, to physics, to time and to measurement. The corpus is a separate body of articles from the physics corpus, with its own menu, and the two are not mixed.

**The corpus's own mathematics.** The corpus is mostly an account of established mathematics, and the part that is its own is collected in the section *New Results* below. It lies in one synthetic chapter, that of the biquaternion algebra, and in the systematic treatment of the number systems: the reading of one algebra under all its natural products, the study of the class of structures those products define, and one theorem about a transform the algebra carries. The rest of the corpus supplies the general theory those constructions use.

## How the Corpus Is Organised

### The Six Parts

The parts are ordered by dependency, and each says what it may and may not use.

| Part | Subject |
|---|---|
| I : Algebra | the objects themselves, built with no distance: sets, functions and relations, logic and proof, cardinality; then groups, rings and fields, linear spaces, algebras, and the further subjects. Carries the **form** and the **algebraic norm**, whose values lie in the ring or the algebra |
| II : Topology | a **distance** placed on each object of Part I: metric and topological spaces, separation and metrisation; then the distance on groups, on rings and fields, on linear spaces, on algebras; then algebraic topology, sheaves and cohomology, algebraic geometry, geometric topology |
| III : Analysis | the two limits that need more than a topology: the **derivative**, which needs a norm, and the **integral**, which needs a measure; then the calculus, the smooth manifolds and the differential topology, the Lie groups, the integration, the analytic functions, the spectral theory, the differential equations, probability and ergodic theory, and the dynamical systems |
| IV : Geometry | the distance as an **object**: its shape, its motions, its figures and its settings, the form-defined classical groups, and the synthesis with analysis |
| V : Catalogues | transversal lists, one kind of object per article, naming each object and pointing to the articles that introduce it |
| VI : Synthetic Studies | one number system at a time, taken through the whole ladder |

### The Spine and the Object Ladder

Each of Parts I, II and III is organised by the **same five-slot spine**, in the same order: Foundations, Groups, Rings and Fields, Linear Spaces, Algebras. The slots are the rungs of the **object ladder**, in which each layer adds exactly one structure to the layer above. The ladder does not stop at Algebras: each part appends its own **further subjects**, and it is there, at the open end of the ladder, that a subject needing a structure introduced later finds its place.

| Slot | Part I : Algebra | Part II : Topology | Part III : Analysis | Part IV : Geometry |
|---|---|---|---|---|
| Foundations | Foundations of Algebra | Foundations of Topology | Foundations of Analysis | Foundations of Geometry |
| Groups | Groups | Topology on Groups | Analysis on Groups | Geometry on Groups |
| Rings and Fields | Rings and Fields | Topology on Rings and Fields | Analysis on Rings and Fields | Geometry on Rings and Fields |
| Linear Spaces | Linear Spaces | Topology on Linear Spaces | Analysis on Linear Spaces | Geometry on Linear Spaces |
| Algebras | Algebras | Topology on Algebras | Analysis on Algebras | Geometry on Algebras |
| Further subjects | Symmetric and anti-symmetric algebras, linear spaces over algebras, sesqualgebras, algebras with a degree-2 form | Topology on algebras with a degree-2 form, algebraic topology, sheaves and cohomology, algebraic geometry, geometric topology | Convexity and order, manifolds and differential topology, differential equations, Lie groups, probability and ergodic theory, dynamical systems | Synthesis of geometry and analysis |

Part IV is not a layer. Geometry adds no structure of its own, but a distance can be placed on the object of every rung, so geometry is **read** at every rung, and its categories follow the same slots in the same order, one category per slot, with the synthesis standing as its further subject. The naming is mechanical in both directions: a Part II category is named *Topology on X* and a Part III category *Analysis on X*, where X is the name of the slot in Part I.

### The Three Rules of Placement

Three rules fix the place of every article.

1. **The ordering rule.** No category may use a structure it has not yet introduced, and no article may use a concept — an example included, since an example is a use — that a later article introduces.
2. **The dependency rule.** The parts are strictly ordered, and algebra, which needs no distance, is the most fundamental.
3. **The revisit rule.** An object re-read through a new structure belongs to the new category, not the old one. The Lie groups need the smooth structure, which Analysis introduces, so they are further subjects of Analysis; the isometries and the form-defined groups are geometry articles once a form is read as a motion.

### The Boundary Tests

Each boundary between two parts gives a local test of what a part may not use. They govern what a part may **reason** with, not what it may name.

- **Distance** is the boundary between algebra and topology. A **form** and its **algebraic norm**, whose value is an element of the ring or the algebra, belong to Algebra; the object turns topological the moment the norm is **selected** to take positive real values and a length or a distance is asked of it. This is the meaning of the statement that **algebra is clean**: Part I has no length, no distance, no positive definiteness, and every concept that would require one is deferred.
- **The derivative and the measure** are the boundary between topology and analysis.
- **A change of intent** is the boundary between analysis and geometry: topology and analysis study the distance as a tool, geometry studies a chosen distance as an object.

### The Groups Inside a Category

A category of Parts I to IV lists its articles in four groups, each of which adds one thing to the group before it, and a fifth that closes it.

| Group | What it holds |
|---|---|
| Theory | the structure itself, read with the product of its elements |
| Operator Theory | the operators on the structure: the left and right multiplications, the derivations, the automorphisms, the sandwich |
| * Theory | the same structure read with an involution on its **elements** |
| * Operator Theory | the operators built from the **involution**, of which the adjoint is the archetype |
| Applications | the concrete instances of the structure, closing the category |

The star names the involutive layer in both cases, and the layer of the elements and the layer of the operators are two structures and not one: an involution on the elements does not by itself produce an adjoint on the operators.

### The Catalogues

Part V is organised by object rather than by structure. Each catalogue is a transversal list of the objects of one kind that the corpus meets — a catalogue of fields collects every field, a catalogue of forms every form with its signature. Its rule is stated once:

> A catalogue names an object and points to the article or articles that introduce it. It introduces nothing and it proves nothing.

The one condition on what a catalogue may list is that the object has been introduced somewhere in Parts I to IV. A catalogue lists examples and non-examples side by side, and the non-examples are what show that each class is a proper subclass of the one above it.

### The Synthetic Studies

Parts I to IV develop the general theory layer by layer, one structure at a time. Part VI reverses the direction and studies one **system** at a time, taking it through the whole ladder. Its systems are the number systems and their relatives, in the order the corpus reaches them, from the Booleans to the octonions. A synthetic study is where a system is shown to support an algebra and a topology but no analysis, or the reverse, and the stopping point is a fact about that system.

### The Successive Paths

The corpus is learnt by **successive paths**. A cycle runs through the six parts at one depth — basic Algebra, basic Topology, basic Analysis, basic Geometry, a first catalogue and a first synthetic study — and then the reader returns to the beginning and runs the same path one rung deeper. The depth is carried by the ladder, not by the cycle count, and a cycle is complete when all six parts have been entered, not when any one of them is finished.

### The Two Exclusions

The corpus excludes applications and physics, and both exclusions have the same reason: a use is not a property of the structure. Numerical analysis, control theory, cryptography as an engineering subject and mathematical finance are not articles. A mathematical concept named after a physical object is admitted on the same terms as any other, and then only for its mathematical content. The clearest case is the **Lorentz group**: it is the group of linear transformations preserving a quadratic form of signature $(3,1)$, and that is a complete definition in pure algebra. What the corpus does not write is *spacetime*, *the speed of light*, *an observer* or *a measurement*. Where a mathematical synonym exists it is preferred: a **hyperbolic rotation** rather than a boost, the **null cone of a quadratic form** rather than a null cone, and **signature** rather than any metrical vocabulary.

## New Results

**Everything in this section is the corpus's own**, and this is where what is new is collected. The corpus is mostly an account of established mathematics, and the algebra below is standard: the corpus does not claim otherwise. Its most developed single system is the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the complexification of the quaternions, a four-dimensional associative algebra over $\mathbb{C}$ with zero divisors. The work begins with the **sesqualgebras**, the corpus's most general new object; it continues with the structures the corpus's construction produces, over the number systems and then in full over the biquaternion algebra; and it closes with one analytic result, a Bochner theorem for the transform the algebra carries. Every statement is proved from the corpus's own definitions, so it needs no experiment; what is new is the organisation of one algebra and its class of products, not the algebra.

### The Sesqualgebras

A **sesqualgebra** is an algebra whose product is linear in the first variable and conjugate-linear in the second, the conjugating map being an involution $\varsigma$ of the base ring:

$$
(\lambda x)y=\lambda(xy),\qquad x(\lambda y)=\varsigma(\lambda)(xy).
$$

The object is the algebra companion of the sesquilinear form, and the two are different: a sesquilinear form takes its values in the scalars, a sesqualgebra in the algebra itself. The datum is the pair $(R,\varsigma)$, and the object is relative to it; for the trivial involution the two scalar rules coincide and the category collapses exactly to the ordinary algebras. The corpus's reformulation is what makes the category tractable: a sesqualgebra over $(R,\varsigma)$ is an $R$-bilinear map $A\times A^{\varsigma}\to A$, where $A^{\varsigma}$ is the **conjugate module** ($\lambda\cdot x=\varsigma(\lambda)x$). The standard example is the derived operation $x\star y=xy^{*}$ of an associative algebra with a conjugate-linear involution, and it is associative exactly when the involution is the identity — which is why the sesquilinear world is not the bilinear one in another notation. The corpus develops the category as its bilinear sibling is developed: the conjugate module, the left and right multiplications with their opposite linearity, the ideals and quotients, the centre, the units and the zero divisors, the derivations, and the algebras with a degree-2 form on top of it.

### Complexoid, quaternioid and biquaternion structures

Construction of non-associative complexoid, quaternioid and biquaternion structures, using some particular products, split into a general, a symmetric and an antisymmetric part.

### The Bochner Theorem for the Biquaternion Transform

The corpus's own analytic result is a theorem about the transform that the biquaternion algebra carries. Bochner's theorem says that a continuous normalised positive-definite function on a group is the Fourier transform of a positive measure; read the other way it says the transform of a positive measure is positive definite. Its proof consumes two properties of the character — that it is multiplicative and that it is unitary — together with one property of the pairing, that the quadratic form carries the conjugation in its **second** slot. In the biquaternion algebra the ingredients are no longer settled in advance: multiplicativity survives every root; the unitarity of the character becomes a condition on the **root of $-1$** carried by the kernel's exponential, and the roots fall into families; and the pairing is chosen among the four the algebra carries.

The corpus's answer is a single condition. The positivity the theorem needs is the positivity of the general plain sesquilinear form, and with that form **the theorem holds exactly for the roots that are skew-adjoint for the Hermitian conjugation** — the scalar imaginary and the real roots — and fails for the genuinely complex roots. The reason is exactly the unitarity of the character: the kernel is the exponential of the root, and it is unitary precisely when the root is skew-adjoint for the Hermitian conjugation. The corpus separates this from a different failure, which tests the multiplicative form and is independent of the root; the two are true statements and they are not the same statement. What is proved is the direction from the measure to the positive-definite function, with the criterion on the root; the converse of Bochner's theorem, that every positive-definite function is the transform of a positive measure, is not claimed.

## What the Corpus Does Not Do

The limits are as clear as the results.

- **The novelty is confined to one chapter.** The corpus is an account of established mathematics, and the part that is its own is one synthetic algebra together with the study of the class of structures its products define. Every other article restates mathematics that was already there.
- **No physics and no application.** The corpus is pure mathematics by rule: no time, no measurement, no observable, no interpretation, and no article about a use of mathematics.
- **The corpus is not an encyclopaedia.** A concept is introduced once, in the category that owns it, and cited afterwards rather than restated. A reader wanting an exhaustive list of its results will not find one in this digest; the digest gives the organisation and the corpus's own contributions, and the menu is the authority on what exists.
- **The corpus is a work in progress.** Articles are written continuously, and this digest deliberately rounds the counts of them, since a census accurate today is stale tomorrow; what is stable is the structure.

## Common Misreadings

1. **It is not a physical theory.** A reader coming from physics will recognise objects in it — the Lorentz group, the null cone, the hyperbolic rotation — but the corpus describes them as algebra and geometry, and no statement in it is about the world.
2. **The biquaternion algebra is not the corpus's discovery.** It is standard. What is new is the systematic reading of one algebra under all its natural products, and the creation of the new structures those products define, the complexoids, the quaternioids and the biquaternions. These are not alternative multiplications of the number system: the field, the quaternion algebra and the biquaternion algebra keep their own product in their own chapter, and each added structure is a new non-associative structure over the same space.
3. **The four general products are distinct operations.** None agrees with another on every pair, and the twelve products built from them are distinct too; a check restricted to real elements sees only ten, because two pairs coincide there.
4. **An algebraic norm is not a length.** It takes its value in the ring or the algebra — the algebraic norm of a biquaternion is a biquaternion — and it belongs to Algebra. The **topological norm**, selected to take positive real values, is what gives a distance, and it belongs to Topology.
5. **A form that multiplies and a form that is definite are two different tools.** The multiplicative form vanishes on nonzero elements; the definite form does not multiply. No function on the algebra is both, and the zero divisors are the reason.
6. **The definitions of the element classes are relative to the product.** A zero divisor, an idempotent and a root are read *of* a product; the same element may satisfy the equation of one product and not of another.
7. **"Interval" has two senses, and the corpus keeps them apart.** An interval is an order-theoretic or lattice object: a convex subset of a linearly ordered set, defined by the order and not by a form. The value of a quadratic form is a different object, defined by the form and not by an order; where the two senses could meet, the corpus writes *the form value*, or *the quadratic form*. A statement about the sign of the form value is therefore never a statement about a lattice interval.
8. **The two involutions are two structures, not one.** The involution on the elements and the adjoint on the operators are different objects, and they need not coincide: an involution on the elements does not by itself produce an adjoint on the operators, and two adjoints of one structure may differ. When the two do agree the representation is a star-representation, and the agreement is proved in the article, never assumed.
9. **Geometry is not a fifth layer.** It adds no structure; it reads the distance of Part II as an object, and its categories follow the same slots as the other parts.
10. **A catalogue proves nothing.** It names objects that have been introduced elsewhere and points to where; it is not an article that introduces a concept of its own.

## Summary

The mathematical corpus is a single account of pure mathematics of about 2,100 articles in six parts. Algebra builds the objects and carries the form and its algebraic norm, whose values lie in the ring or the algebra; Topology places a distance on each object; Analysis uses the derivative and the measure; Geometry reads the distance as an object; Catalogues gather the objects of the first four parts into transversal lists; and Synthetic Studies take one number system at a time through the whole ladder. Parts I to III share one five-slot spine — Foundations, Groups, Rings and Fields, Linear Spaces, Algebras — each adding its further subjects after it. Three rules fix the placement of every article: no category may use a structure it has not introduced, the parts are strictly ordered, and an object re-read through a new structure belongs to the new category. The boundaries give local tests: distance between algebra and topology, the derivative and the measure between topology and analysis, and a change of intent between analysis and geometry. The corpus is pure mathematics, with no application and no physics.

The corpus's most developed single system is the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, associative with zero divisors and isomorphic to the $2\times2$ complex matrices. Its four general products carry four forms, two of which do the two jobs the corpus keeps apart: the multiplicative form multiplies, the Hermitian form is definite, and no function is both. The four products split into twelve distinct products, the twelve structures of the biquaternion space, of which two satisfy the identity of their kind and six fail it. The same construction is run over the smaller number systems, and it creates the corpus's new structures beside the classical product of each: two for the complex field, two for the split-complex ring, six for the quaternion algebra and twelve for the biquaternion algebra, named the **complexoids**, the **split-complexoids**, the **quaternioids** and the **biquaternions** in that order, and all but the classical product are non-associative. The element classes are relative to the product, and the corpus studies them product by product, with the idempotents, the nilpotents, the zero divisors, the roots and the Peirce decomposition. The corpus also develops the **sesqualgebras**, the algebras whose product is conjugate-linear in the second slot, as the algebra companion of the sesquilinear form, with the conjugate module $A^{\varsigma}$ turning every statement into one about a bilinear map $A\times A^{\varsigma}\to A$; and it proves a **Bochner theorem** for the biquaternion transform, in the general plain sesquilinear form, for the roots that are skew-adjoint for the Hermitian conjugation, and in the measure-to-function direction, the representability half being left open. Its statement is also continuous: on a finite abelian group the criterion is group-dependent, since a group whose characters are all central makes every root positive definite.

Most of the corpus restates established mathematics, ordered by dependency. What it adds is the organisation of one algebra and the study of the class of structures its products define, proved from the definitions, so that it needs no experiment and is where the corpus's contribution lies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| general, symmetric, antisymmetric; plain, quaternionic; algebra, sesqualgebra | the three parts in the name of each of the twelve biquaternion structures, in that order: the operation, the first slot, and the family, the third part naming an algebra over $\mathbb{C}$ or a sesqualgebra over $(\mathbb{C},\bar\cdot)$ |
| $2,\,2,\,6,\,12$ | the number of structures the construction creates over the complex numbers, the split-complex numbers, the quaternions and the biquaternions, named the complexoids, the split-complexoids, the quaternioids and the biquaternions; all but the classical product are non-associative |
| $\varsigma$, $A^{\varsigma}$ | involution of the base ring of a sesqualgebra, and its conjugate module |
| Part I to VI | Algebra, Topology, Analysis, Geometry, Catalogues, Synthetic Studies |
| Foundations, Groups, Rings and Fields, Linear Spaces, Algebras | the five-slot spine shared by Parts I to III |
| Theory, Operator Theory, * Theory, * Operator Theory, Applications | the five groups of a category |
