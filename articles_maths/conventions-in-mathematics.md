# __Conventions in Mathematics__

## Introduction

This article gathers the conventions the mathematical articles assume: the symbols, the arithmetic conventions, the shape of a generic element and its coefficients, the marks reserved for the conjugations of an algebra with an involution and for the adjoint of an operator, the typographic rules of the source, and the working conventions of the corpus itself — the menu, the groups inside a category, the article files and the skeleton.

They are stated once, here, so that no other article need repeat them. How the articles are organised into the six parts and their categories is the subject of the companion article *Introduction to Mathematics*; this one is the reference for the elements, the marks, the glyphs and the layout.

## Notational Conventions

The conventions below are those used throughout the corpus. They are stated once, here, so that the other articles need not repeat them.

### Symbols

| Symbol | Meaning |
|---|---|
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ | the naturals, integers, rationals, reals, complex numbers |
| $\mathbb{D}$ | the split-complex numbers, $\mathbb{R}[x]/(x^2-1)$ |
| $\mathbb{D}'$ | the dual numbers, $\mathbb{R}[x]/(x^2)$ |
| $\mathbb{H}$ | the real quaternions |
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternions, $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ |
| $\mathbb{B}$ | the biquaternions, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\mathbb{H}_{\mathbb{D}}$ | the split-biquaternions, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\mathbb{O}$ | the octonions |
| $G$ | a group; $R$ a ring; $k$, $F$ a field; $V$ a vector space; $M$ a module; $A$ an algebra |
| $\mathrm{G}, \mathrm{H}, \mathrm{SL}_n$ | Lie algebras |
| $\mathrm{M}, \mathrm{P}$ | ideals and prime ideals |
| $\operatorname{Sym}(X), \operatorname{Aut}(X)$ | symmetric group of a set; automorphism group of a structure |
| $\operatorname{End}(V), \operatorname{Der}(A), \operatorname{Inn}(A), \operatorname{Out}(A)$ | endomorphisms, derivations, inner and outer automorphisms |
| $GL, SL, PGL, O, SO, U, SU, Sp$ | the classical groups |
| $T(V), S(V), \Lambda(V), Cl(V,Q)$ | tensor, symmetric, exterior and Clifford algebras |
| $V^{\otimes n}, S^n V, \Lambda^n V$ | tensor, symmetric and exterior powers |
| $B(v,w), Q(v), N(x)$ | bilinear form, quadratic form, norm |
| $\bullet$ | the symmetrised (Jordan) product, $x \bullet y = \tfrac{1}{2}(xy + yx)$; the circle $\circ$ is reserved for the composition of maps |
| $\bar{\cdot}, {}^{\natural}, {}^{*}, {}^{\flat}, {}^{\dagger}$ | the conjugations of an algebra with an involution, and the adjoint of an operator; *The conjugations and the adjoint* below fixes their meanings |
| $\tilde\Pi$ | an idempotent, a projector or a pure state, and the minimal left ideal it generates |
| $\tilde P, \tilde q, \tilde Q$ | a generic element of the algebra: the quaternion, split-quaternion, biquaternion or split-biquaternion one |

### Groups, rings and operations

A group is written multiplicatively by default, with unit $e$ and inverse $x^{-1}$, and additively when it is the underlying group of a ring, with zero $0$ and inverse $-x$. A ring is a triple $(R, +, \cdot)$; a ring need not be commutative and need not have a unit, and the article that introduces it says which conventions it adopts. A field is a commutative ring with $1 \neq 0$ in which every nonzero element is invertible. A module is written with its scalars on the left unless the article says otherwise, and the side matters as soon as the ring is non-commutative. Products are written by juxtaposition: $ab$ for the product in a group or an algebra, $fv$ for the action of a scalar on a vector. The **symmetrised (Jordan) product** is written with a bullet, $x \bullet y = \tfrac{1}{2}(xy + yx)$, and the circle $\circ$ is kept for the **composition of maps**, as in $\mathrm{H}_{\tilde Q}\circ\mathrm{H}_{\tilde R}$.

### LaTeX and typesetting

The articles are rendered with KaTeX on the page, and the following rules are observed in the source.

- Inline mathematics is written between single dollars, and display mathematics between double dollars on lines of their own.
- Inline mathematics never spans a line break. If a formula is too long, it is displayed.
- Display mathematics inside a list is indented four spaces.
- A prime is never written immediately after a symbol that also carries a subscript: the form `q'_0^2` is not written. The prime is applied to the symbol first, and the subscript follows it.
- Tables are Markdown tables. A LaTeX array is never used for a table.
- Every heading that introduces a comparison or a classification is a real `###` heading, and the objects are defined before they are tabulated.
- **Bold marks the result.** In a Remark that states a verdict, the clause carrying the outcome is
  set in bold, `**...**`, the object of the sentence staying in plain roman: *the subspace **is a
  commutative Jordan algebra over $\mathbb{R}$ of degree two***. A statement already displayed as a
  Theorem, a Proposition or a Proof is not bolded; the convention applies to the prose of a Remark and
  to the lead sentence of a section that states an outcome.
- The macros `\dddot` and `\slashed` are available. The characters `|`, `{`, `}`, `<` and `>` inside mathematics need no escaping.
- A malformed formula is rendered in red on the page rather than reported as an error, so mathematics is checked by eye and not by the absence of a warning.

## Algebraic Conventions

The conventions below fix how the elements themselves are written: the case and the tilde that name its
algebra, the shape of a generic element and the letters of its coefficients, the marks reserved for the
conjugations, and the symbol of the idempotents.

### The element and its coefficients

The case and the tilde of the glyph are fixed first, and the element is written after. A generic element is preferably written so that the glyph alone identifies its algebra, two features being read together: the **case** separates a real scalar from a complex one, and a **tilde** marks the quaternionic factor.

| System | Name | Generic element | Coefficients |
|---|---|---|---|
| $\mathbb{2}$ | Booleans | $\alpha, \beta, \dots$ | — |
| $\mathbb{N}$ | naturals | $n, m, \dots$ | — |
| $\mathbb{Z}$ | integers | $n, m, \dots$ | — |
| $\mathbb{Q}$ | rationals | $a, b, c, \dots$ | — |
| $\mathbb{R}$ | reals | $a, b, c$ | — |
| $\mathbb{C}$ | complex numbers | $A = a + ia'$, $B = b + ib'$ | real, $a, a'$ |
| $\mathbb{D}$ | split-complex numbers | $A = a + ja'$, $B = b + jb'$ | real, $a, a'$ |
| $\mathbb{D}'$ | dual numbers | $A = a + \varepsilon a'$, $B = b + \varepsilon b'$ | real, $a, a'$ |
| $\mathbb{H}$ | quaternions | $\tilde q = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$ | real |
| $\mathbb{H}_{\mathrm{s}}$ | split-quaternions | $\tilde q = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$ | real |
| $\mathbb{B}$ | biquaternions | $\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ | complex, $Q_\mu = q_\mu + iq'_\mu$ |
| $\mathbb{H}_{\mathbb{D}}$ | split-biquaternions | $\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ | split-complex, $Q_\mu = q_\mu + jq'_\mu$ |
| $\mathbb{O}$ | octonions | $\tilde o = o_0e_0 + o_1e_1 + \cdots + o_7e_7$ | real |

Four rules are read off the table. **A complex element carries a majuscule**, $A$ or $B$, the case naming the scalar sector: an upper-case glyph has a scalar sector larger than the reals, a lower-case one has the reals. **The second coordinate of a complex element carries a prime**, $A = a + ia'$, with $j$ in place of $i$ for the split-complex numbers and $\varepsilon$ for the dual numbers. **The four quaternionic elements carry a tilde**: lower case for the quaternions and the split-quaternions, $\tilde q$, and upper case for the biquaternions and the split-biquaternions, $\tilde Q$. And **the arithmetic systems and the reals carry a letter that is theirs alone**: $\alpha, \beta$ the Booleans, $n, m$ the naturals and the integers, and $a, b, c$ the rationals and the reals — a letter, no prime, no tilde, no coefficient sector, since these elements are not written as linear combinations.

For the biquaternions, whose basis is $e_0, e_1, e_2, e_3$ with $e_0 = 1$ the unit,

$$
\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3, \qquad Q_\mu = q_\mu + iq'_\mu,
$$

where the four coefficients $Q_\mu$ are complex, and each of them splits into a real part $q_\mu$ and an imaginary part $q'_\mu$. **The two parts of a coefficient share its letter**, the imaginary part carrying a prime. The shape is the same in the quaternion systems; only the coefficient sector changes, and the table above gives the element and the coefficients of each system. The unit $e_0$ is the identity in the two quaternion systems, and the real and the imaginary part of a coefficient may be read off only where the scalar sector is larger than the reals, which is the case in $\mathbb{C}$ and $\mathbb{B}$ and not in $\mathbb{R}$ or $\mathbb{H}$.

The case and the tilde are read independently, and the glyph of a generic element is the two together: $a$ is real, $A$ complex, split-complex or dual, $\tilde q$ quaternion or split-quaternion, $\tilde Q$ biquaternion or split-biquaternion, and $\tilde o$ octonion.

**The coordinates carry the letter of the element.** The components of a generic element are written with the same letter as the element and a subscript: $q_\mu$ for $\tilde q$, $Q_\mu = q_\mu + iq'_\mu$ for $\tilde Q$, and $o_\mu$ for $\tilde o$; a Euclidean vector part assembled from the non-scalar components carries the bold letter, $\mathbf{q}$, $\mathbf{Q}$ or $\mathbf{o}$; and a plain real variable is $a$, $b$ or $c$. In the synthetic studies of Part VI the letters $x, y$ and $z$ name neither an element nor a coordinate of any system: they appear there only as a formal indeterminate, as in $\mathbb{R}[x]/(x^2-1)$, or inside the name of an operator, a map or a function that the article itself defines.

This is a **preferred convention** — a preference, not a strict rule, not to be enforced by rewriting other articles: the basis $e_0, \dots, e_3$, the central unit $i$, the Euclidean vector $\mathbf{q}$, the coefficients $q_\mu, q'_\mu$, indices such as $\mu, \nu, k$, structure constants, and the individual elements an article defines keep the symbols that article gives them. Where the constructions that share a glyph must be told apart — the complex from the split-complex and the dual, the quaternion from the split-quaternion, the biquaternion from the split-biquaternion — the glyph is qualified by a subscript, as in $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{H}_{\mathbb{D}}$.

### The conjugations and the adjoint

The biquaternion algebra carries four natural involutions, all of them used in the series, together with the adjoint of an operator, which belongs to the operators and not to the algebra:

| Map | Mark | What it is |
|---|---|---|
| complex conjugation | $\bar{\cdot}$ | the involution of the base, extended to the element |
| quaternion conjugation | ${}^{\natural}$ | the intrinsic conjugate: it fixes the scalars and negates the vectors |
| Hermitian conjugation | ${}^{*}$ | the involution of the algebra, $\bar{\cdot}\circ{}^{\natural}$ |
| anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | the negative of the star |
| operator adjoint | ${}^{\dagger}$ | the general adjoint of an operator, $(L_a)^{\dagger} = L_{a^{*}}$; where the adjoint is obviously the one of the positive definite form the two marks are written together, the dagger first, $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$ |

Which of the marks has a sense depends on the system, since a mark degenerates wherever the structure it conjugates is absent. The four examples below fix it system by system.

**The complex numbers $\mathbb{C}$.** Only the bar has a sense, the algebra carrying a single non-trivial involution:

$$
\bar A = a - ia' .
$$

**The split-complex numbers $\mathbb{D}$.** Only the bar has a sense:

$$
\bar A = a - ja' , \qquad j^2 = +1 .
$$

**The quaternions $\mathbb{H}$ and the split-quaternions $\mathbb{H}_{\mathrm{s}}$.** Only the natural sign has a sense, the coefficients being real and the conjugation intrinsic to the quaternion factor, and the same formula is read on the two sets of units:

$$
\tilde q^{\natural} = q_0e_0 - q_1e_1 - q_2e_2 - q_3e_3 , \qquad e_k^2 = -e_0 \ (\mathbb{H}) , \qquad e_1^2 = -e_0 , \ e_2^2 = e_3^2 = +e_0 \ (\mathbb{H}_{\mathrm{s}}) .
$$

**The biquaternions $\mathbb{B}$ and the split-biquaternions.** All four have a sense, the bar conjugating the coefficient, complex in $\mathbb{B}$ and split-complex in the split-biquaternions:

$$
\bar{\tilde Q} = \bar Q_0e_0 + \bar Q_1e_1 + \bar Q_2e_2 + \bar Q_3e_3 , \qquad \tilde Q^{\natural} = Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3 ,
$$

$$
\tilde Q^{*} = \overline{\tilde Q^{\natural}} = \bar Q_0e_0 - \bar Q_1e_1 - \bar Q_2e_2 - \bar Q_3e_3 , \qquad \tilde Q^{\flat} = -\tilde Q^{*} .
$$

The dagger is the **general adjoint**: it acts on an operator and not on an element, and it is the same in every system. It is the general mark under which the several adjoints of the corpus fall — one for each form, one for each sandwich — and where the adjoint in view is obviously the one of the positive definite form the text writes the two marks together, the dagger first and the star second, so that the coincidence is apparent: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$ and $(\Theta_{\tilde{Q}})^{\dagger}=(\Theta_{\tilde{Q}})^{*}=\Theta_{\tilde{Q}^{*}}$.

### The idempotent convention

The convention of *The element and its coefficients* fixes the case and the tilde of a generic element. The idempotents carry a symbol of their own, and the corpus uses it throughout.

An **idempotent** of the algebra is an element $\tilde\Pi$ with $\tilde\Pi^2 = \tilde\Pi$; a **projector** is a Hermitian idempotent, $\tilde\Pi^{*} = \tilde\Pi$, and the rank-one projectors of $\mathbb{M}_+$, the Hermitian subspace, are the **pure states**,

$$
\tilde\Pi_{1,2}(\hat\mu) = \tfrac{1}{2}\bigl(e_0 \pm i\,\hat\mu\bigr), \qquad \hat\mu \in \mathbb{R}^3,\ |\hat\mu| = 1 .
$$

The standard pair of the algebra is

$$
\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3), \qquad \tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3), \qquad \tilde\Pi_1 + \tilde\Pi_2 = e_0, \qquad \tilde\Pi_1\tilde\Pi_2 = 0 ,
$$

and the two nilpotent matrix units of its Peirce decomposition are $\tilde R = \tfrac12(ie_1 - e_2)$ and $\tilde T = \tfrac12(ie_1 + e_2)$. The lower-case letters $p, q$ for the standard pair are retired, and a minimal left ideal is written $\mathbb{B}\tilde\Pi_1$ and never $\mathbb{B}p$; the classification, the Peirce decomposition and the basis $\{\tilde\Pi_1, \tilde T\}$ are those of *Biquaternion Idempotents and Projections* and *Biquaternion Ideals and Peirce Decomposition*.

The family $\tilde\Pi_{1,2}(\hat\mu)$, written with its argument, is the two-sphere of pure states of the algebra in view; the central idempotents $\tfrac12(1\pm j)$ of the split-complex algebra are the separate pair $\tilde\Pi_{3,4}$.

The involution here is the star on the elements, as *The conjugations and the adjoint* fixes it, and *Conventions in the Biquaternion Universe* writes the same involution with the same star, $\tilde\Pi^{*} = \tilde\Pi$: the two corpora agree on the mark, and it is the dagger that is confined to the operators.

A non-zero idempotent $\tilde\Pi$ generates the **minimal left ideal** $\mathbb{B}\tilde\Pi$; the classification of the idempotents, the polarisation identity, the Peirce decomposition and the projective geometry of the pure states are those of *Biquaternion Idempotents and Projections* and its companions.

The upper-case tilde is therefore **split between two roles**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde\Pi$ | an idempotent, a projector or a pure state, and the minimal left ideal $\mathbb{B}\tilde\Pi$ it generates |
| $\tilde P$ | a *generic* element wherever a statement holds for every element |

The generic element keeps its $\tilde P$ in the statements that hold for all elements: the trace pairing $\operatorname{Tr}(\tilde P\tilde Q) = 2\operatorname{Sc}(\tilde P\tilde Q)$, the commutator bracket $[\tilde P, \tilde Q] = \tilde P\tilde Q - \tilde Q\tilde P$, the general plain bilinear form $B(\tilde P, \tilde Q)$ and the multiplicativity $N(\tilde P\tilde Q) = N(\tilde P)N(\tilde Q)$. Both roles are inherited from *Biquaternion Idempotents and Projections* and its companions, which write the idempotent $\tilde\Pi$ and the generic element $\tilde P$ side by side.

The convention is one of **notation, not of substance**: an element written $\tilde\Pi$ is not a different kind of object from one written $\tilde Q$, only an element known to be idempotent, and the glyph records that knowledge at the point of use. Where a passage needs a generic idempotent variable it may write $\tilde\Pi$, and where it needs a generic element it writes $\tilde P$ or $\tilde Q$.

## Conventions of the Corpus Itself

The corpus has a small number of working conventions that are not mathematical.

**The menus.** Every article is registered in exactly one menu: `maths.md` for the mathematical corpus and `physics.md` for the physics corpus. An entry has the form of a link to the article followed by a comment that lists the contents of the article in outline. The mathematical menu opens with the two articles that describe the corpus rather than belonging to one of them — *Introduction to Mathematics* and this one — placed outside the parts. An entry that begins with `+` is a **planned** article, one that is registered in the menu and not yet written; an entry without the marker has its article on disk.

**The groups inside a category.** A category of Parts I to IV lists its articles in four groups, each of which adds one thing to the group before it. The group `- Theory` holds the structure itself, read with the product of its elements. The group `- Operator Theory` holds the operators on that structure — the left and right multiplications, the derivations, the automorphisms, the actions and the sandwich — and adds an operator layer and nothing else. The group `- * Theory` holds the same structure read with an involution on its **elements**. The group `- * Operator Theory` holds the operators built from the **involution**, of which the adjoint is the archetype.

**The two involutions.** The star names the involutive layer in both groups, and the layer of the elements and the layer of the operators are two structures and not one: the involution of `- * Theory` sits on the elements and the adjoint of `- * Operator Theory` sits on the operators. They need not coincide: an involution on the elements does not by itself produce an adjoint on the operators, and two adjoints of the same structure may differ — the transpose and the Hermitian adjoint of a matrix are both adjoints, taken with respect to different pairings. When the two do agree the representation is a `*`-representation, and the agreement is proved in the article, never assumed by the menu.

**The order and the fill rule.** The four groups are placed in the order above, and the group `- Applications`, which holds the concrete instances of the structure, closes the category. The groups `- Operator Theory` and `- * Operator Theory` are present in a category whenever it has an operator layer, and the group `- * Theory` is present in every category of Parts I to IV, whether or not it yet holds an article.

**The category names and numbers.** The menu numbers its categories, and an article elsewhere in the corpus may address one by number rather than by name: *category n* means the n-th category of the mathematical menu, read in order. This article refers to categories by **name** throughout, because the names are the stable thing and the numbers shift whenever a category is inserted or split. A reader who meets a bare number in another article can resolve it in the menu.

**The article files.** The corpus is split into two collections, each with its own folder: a mathematical article is a file `articles_maths/<slug>.md` and a physical article is a file `articles_physics/<slug>.md`, where the slug is the title in lower case with hyphens in place of spaces and punctuation. The folder and the menu agree — an article lies in the folder whose menu lists it, and no article lies in both.

**The article skeleton.** Every article opens with its title as the first heading, followed by an *Introduction* that states what the article does and what it assumes, then the thematic sections, and closes with three sections in this order: *Summary*, *Summary of Notation*, and *Further Reading*. The introduction states the article's boundaries — what it deliberately does not cover, and where the reader will find it.

**Cross-references and boundaries.** A concept is introduced once, in the category that owns it, and referred to afterwards rather than restated. Articles do not duplicate the content of other articles; they cite them. Every article that touches a structure belonging to a later part states the deferral explicitly, which is the mechanism by which Rule 1 is enforced.

**The word "interval".** Two different objects share the word, and the corpus keeps them apart. In the mathematical corpus an **interval** is an order-theoretic or lattice object: a convex subset of a linearly ordered set, the interval $[a,b]=\{x:a\le x\le b\}$ of a lattice or of a poset of effects, defined by the order and not by a form. In the physical corpus the **interval** is the value of the quadratic form, $N(\tilde Q)=(ic\,t)^2+\mathbf x^2=\mathbf x^2-c^2t^2$ on the material sector, defined by the form and not by an order. A statement about the sign of the interval is therefore never a statement about a lattice interval, and a lattice interval is never the line element; where the two senses could meet, the corpus writes *the form value* or *the quadratic form* for the physical one.

## Summary

The conventions are of two kinds: the mathematical notation, and the working conventions of the corpus.

A generic element of a number system is written as a linear combination of the basis with its coefficients in
the scalar sector of the system, the biquaternion element being $\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$
with $Q_\mu = q_\mu + iq'_\mu$. The generic element of a system carries a letter of its own: $\alpha, \beta$ for the Booleans, $n, m$ for the naturals and the integers, $a, b, c$ for the rationals and the reals, and $A = a + ia'$, $B = b + ib'$ for the commutative two-parameter systems. The notation is fixed here above all for the conjugations, which is where the corpus has the most marks to keep apart, and for the number systems, whose glyphs carry two bits each. An algebra with a degree-2 form carries an intrinsic conjugate, the map that negates its vectors and fixes its scalars; it is written with a **natural sign**. The involution of the base extends to the coefficients and is written with a **bar**. Their composite is the Hermitian anti-automorphism that makes the algebra a Hilbert algebra, written with a **star**; its negative is the **anti-Hermitian** conjugation, written **flat**; and the **dagger** is the adjoint of an operator, written on operators and never on the elements. The star and the bar commute, $^{*} = \bar{\cdot}\circ{}^{\natural} = {}^{\natural}\circ\bar{\cdot}$, the flat is $\flat = -{}^{*}$, and $\{\mathrm{id}, \bar{\cdot}, {}^{\natural}, {}^{*}\}$ is a Klein four-group while the flat stands outside it. On a base whose involution is the identity the bar is the identity map and the star coincides with the natural sign.

On the number systems the **case** records whether the commuting scalar sector is larger than the reals and the **tilde** records the presence of the quaternionic factor, and the two are read independently: $a$ is real, $A$ complex or split-complex or dual, $\tilde q$ quaternion or split-quaternion, and $\tilde Q$ biquaternion or split-biquaternion. The **idempotents** carry a symbol of their own: $\tilde\Pi$ is an idempotent, a projector or a pure state, and the minimal left ideal it generates, while $\tilde P$ is the generic element of a statement that holds for every element. The upper-case tilde is thus split between two roles, and the split is deliberate.

The working conventions are the corpus's own. Every article is registered in exactly one menu, with a comment that outlines it, and a leading `+` marks a planned article. The four groups of a category — Theory, Operator Theory, `*` Theory and `*` Operator Theory — each add one thing to the group before, the star naming the involutive layer on the elements and then on the operators, so that the last group holds the operators built from the involution, and the group `Applications` closes the category. A concept is introduced once, in the category that owns it, and is cited afterwards rather than restated; every deferral to a later part is stated explicitly, which is how the ordering rule of *Introduction to Mathematics* is enforced. Each article opens with its title and an Introduction and closes with Summary, Summary of Notation and Further Reading.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar{\cdot}$ | complex conjugation: the involution of the base, extended to the element |
| ${}^{\natural}$ | quaternion conjugation: the intrinsic conjugate of the algebra |
| ${}^{*}$ | Hermitian conjugation, the composite of the bar and the natural sign |
| ${}^{\flat} = -{}^{*}$ | anti-Hermitian conjugation |
| ${}^{\dagger}$ | the general adjoint of an operator, of which the star is the instance in the positive definite form; written on operators and never on elements |
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}, \mathbb{O}$ | the number systems of the corpus, in the order the corpus reaches them |
| lower case, upper case | the scalar sector is the reals, or larger than the reals |
| tilde | the presence of the quaternionic factor |
| $\alpha, \beta$; $n, m$; $a, b, c$ | the generic elements of the Booleans, the naturals and the integers, and the rationals and the reals |
| $A = a + ia'$, $B = b + ib'$ | the generic element of a commutative two-parameter system, with $j$ or $\varepsilon$ in place of $i$, and the imaginary coefficient carrying a prime |
| $\tilde\Pi$ | an idempotent, a projector or a pure state, and the minimal left ideal it generates |
| $\tilde\Pi_1, \tilde\Pi_2$ | the standard orthogonal idempotents, $\tilde\Pi_1 = \tfrac{1}{2}(e_0+ie_3)$, $\tilde\Pi_2 = \tfrac{1}{2}(e_0-ie_3)$ |
| $\tilde P$ | the generic element of the algebra, in a statement that holds for every element |
| `- Theory`, `- Operator Theory`, `- * Theory`, `- * Operator Theory` | the four groups of a category, in that order |
| `- Applications` | the group that closes a category with the concrete instances of its structure |
| `+` | a planned article, registered in the menu and not yet written |
| `articles_maths/<slug>.md` | the file of a mathematical article; the slug is the title in lower case with hyphens |
| Introduction, thematic sections, Summary, Summary of Notation, Further Reading | the skeleton of every article |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853). The original formulation, and the source of the quaternion conjugation and its notation.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution, the first and the second kind, and the classification of their involutions.
- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for a notation fixed once and used without variation.
- Donald E. Knuth, *The TeXbook* (Addison-Wesley, 1984). The typographic conventions the source of the corpus follows.
