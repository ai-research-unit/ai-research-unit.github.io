# __Conventions of the Indices, the Notation and the Corpus__

## Introduction

This article closes the series with the marks that are read on a glyph rather than on the object: the superscript tokens, the subscript rules and their admitted forms, the working conventions of the corpus and the typography of the source. It assumes the six companions, whose glyphs it indexes.

The superscripts come first because they are two tokens and nothing else; the subscripts next, because their rule depends on the derivation convention fixed in *Conventions of the Operators and the Differential Calculus*. The working conventions of the corpus follow — the menus, the groups inside a category, the article files, the skeleton and the boundaries — and the typography closes the article.

The article is the last of the seven and the index of the notation: the table below collects the tokens and the working marks that belong to the corpus rather than to the algebra, while the table of *Conventions in Mathematics* collects the glyphs of the algebra.

## The Superscripts

Two superscript tokens run beside the marks of the elements and the marks of the conjugations, on the glyphs of elements and algebras, and neither is to be read for the other:

| Token | Written on | Meaning |
|---|---|---|
| $^{\mathrm{fop}}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $^{\mathrm{opp}}$ | an algebra name | the opposite algebra, the algebra with the reversed product |

Two further upright superscripts belong to objects outside the algebra — $\mathrm{fn}$ on a function and $\mathrm{spin}$ on a group element — and are recorded in §*Summary of Notation*.

**The mark, and its one use.** The marks of the elements say what a glyph **is**, not that it is an **operator** (*Conventions of the Operators and the Differential Calculus*, §*The Operators*). The single exception is the **Fock layer** of the physical corpus, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the upright superscript $\mathrm{fop}$, set on the glyph:

$$
a^{\mathrm{fop}},\quad b^{\mathrm{fop}},\quad a^{\mathrm{fop}\dagger},\quad \psi^{\mathrm{fop}},\quad N^{\mathrm{fop}},\quad H^{\mathrm{fop}},\quad F^{\mathrm{fop}},\quad Q^{\mathrm{fop}},\quad U^{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p$, the position $x$, the spin $S$ and the parity, charge-conjugation and reversal maps $P$, $C$ and $T$ carry no superscript, because each keeps the glyph of its element or is a map with a glyph of its own.

**It combines with the dagger, the mark first.** The dagger is the general adjoint (*Conventions of the Operators and the Differential Calculus*, §*The Operators*). Where both marks fall on one glyph the Fock mark comes first and the adjoint follows, $(a^{\mathrm{fop}})^{\dagger}$, contracted to $a^{\mathrm{fop}\dagger}$; the dagger alone never marks a glyph as an operator, and the superscript alone never asserts self-adjointness.

**The opposite algebra carries a different token.** The **opposite algebra**, whose multiplication is reversed, $a\cdot b=ba$, carries the superscript $\mathrm{opp}$ — $A^{\mathrm{opp}}$, $\mathbb{B}^{\mathrm{opp}}$, $M_n(D)^{\mathrm{opp}}$ — and it is the **algebra name** that takes the mark; the Fock token $\mathrm{fop}$ marks a Fock-operator glyph. The two meanings are separated by the token itself and not by context.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}_{\mathrm{r}}$, because a bare underscore would take the first character alone.

**A subscript is never a partial derivative.** The subscript marks a component or a label, a partial derivative is written with $\partial$, and the rule is fixed in *Conventions of the Operators and the Differential Calculus*, §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the units, the roots, the idempotents and the nilpotents as well as the general elements: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}_{\mathrm{r}}$ and $\tilde U_{\mathrm b}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$. In the reduced biquaternion layer the sign belongs to the idempotent pair and to its coordinates, $\Pi_\pm$, $Q_{+}$ and $Q_{-}$, the two basis coordinates carrying the triangles, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and a numbered element putting its number first in either case, $Q_{1+}$ and $Q_{1\blacktriangle}$; the element they build is $\breve Q$. The sign is read with the glyph, and no identity is implied between the pairs: $\tilde Q_\pm$ names the two quaternionic components of a split-biquaternion, $\vec Q_\pm$ their vector parts, and $Q_\pm$ the idempotent coordinates of $\breve Q$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $\tilde\Pi_\pm$ |
| an upright word | $\mathbb{B}_{\mathrm{r}}$, $\tilde U_{\mathrm b}$ |
| a grouped expression | $Q_{n+1}$ |

The decorations that may stand in the subscript slot are these: all 451 distinct glyphs of the KaTeX 0.16.9 symbol table, one entry per glyph, with a single command written where several commands draw the same glyph. An entry that takes an argument is shown on $n$, and an entry that is text is written inside \text.

**Binary operators.** ${}_{\pm}$, ${}_{\times}$, ${}_{\div}$, ${}_{\dagger}$, ${}_{\ddagger}$, ${}_{\mp}$, ${}_{\dotplus}$, ${}_{\setminus}$, ${}_{\ast}$, ${}_{\circ}$,
${}_{\bullet}$, ${}_{\land}$, ${}_{\lor}$, ${}_{\cap}$, ${}_{\cup}$, ${}_{\wr}$, ${}_{\uplus}$, ${}_{\sqcap}$, ${}_{\sqcup}$, ${}_{\oplus}$,
${}_{\ominus}$, ${}_{\otimes}$, ${}_{\oslash}$, ${}_{\odot}$, ${}_{\circledcirc}$, ${}_{\circledast}$, ${}_{\circleddash}$, ${}_{\boxplus}$, ${}_{\boxminus}$, ${}_{\boxtimes}$,
${}_{\boxdot}$, ${}_{\intercal}$, ${}_{\veebar}$, ${}_{\barwedge}$, ${}_{\diamond}$, ${}_{\cdot}$, ${}_{\star}$, ${}_{\divideontimes}$, ${}_{\ltimes}$, ${}_{\rtimes}$,
${}_{\leftthreetimes}$, ${}_{\rightthreetimes}$, ${}_{\curlyvee}$, ${}_{\curlywedge}$, ${}_{\Cap}$, ${}_{\Cup}$, ${}_{\lessdot}$, ${}_{\gtrdot}$, ${}_{\triangleright}$, ${}_{\bigtriangledown}$,
${}_{\triangleleft}$, ${}_{\bigcirc}$, ${}_{\amalg}$, ${}_{\doublebarwedge}$

**Relations.** ${}_{\lt}$, ${}_{\gt}$, ${}_{\in}$, ${}_{\ni}$, ${}_{\backepsilon}$, ${}_{\propto}$, ${}_{\mid}$, ${}_{\nmid}$, ${}_{\parallel}$, ${}_{\nparallel}$,
${}_{\therefore}$, ${}_{\because}$, ${}_{\sim}$, ${}_{\backsim}$, ${}_{\nsim}$, ${}_{\eqsim}$, ${}_{\simeq}$, ${}_{\cong}$, ${}_{\ncong}$, ${}_{\approx}$,
${}_{\approxeq}$, ${}_{\asymp}$, ${}_{\Bumpeq}$, ${}_{\bumpeq}$, ${}_{\doteq}$, ${}_{\Doteq}$, ${}_{\fallingdotseq}$, ${}_{\risingdotseq}$, ${}_{\eqcirc}$, ${}_{\circeq}$,
${}_{\triangleq}$, ${}_{\equiv}$, ${}_{\le}$, ${}_{\ge}$, ${}_{\leqq}$, ${}_{\geqq}$, ${}_{\lneqq}$, ${}_{\gneqq}$, ${}_{\ll}$, ${}_{\gg}$,
${}_{\between}$, ${}_{\nless}$, ${}_{\ngtr}$, ${}_{\nleq}$, ${}_{\ngeq}$, ${}_{\lesssim}$, ${}_{\gtrsim}$, ${}_{\lessgtr}$, ${}_{\gtrless}$, ${}_{\prec}$,
${}_{\succ}$, ${}_{\preccurlyeq}$, ${}_{\succcurlyeq}$, ${}_{\precsim}$, ${}_{\succsim}$, ${}_{\nprec}$, ${}_{\nsucc}$, ${}_{\subset}$, ${}_{\supset}$, ${}_{\subseteq}$,
${}_{\supseteq}$, ${}_{\nsubseteq}$, ${}_{\nsupseteq}$, ${}_{\subsetneq}$, ${}_{\supsetneq}$, ${}_{\sqsubset}$, ${}_{\sqsupset}$, ${}_{\sqsubseteq}$, ${}_{\sqsupseteq}$, ${}_{\vdash}$,
${}_{\dashv}$, ${}_{\perp}$, ${}_{\vDash}$, ${}_{\Vdash}$, ${}_{\Vvdash}$, ${}_{\nvdash}$, ${}_{\nvDash}$, ${}_{\nVdash}$, ${}_{\nVDash}$, ${}_{\vartriangleleft}$,
${}_{\vartriangleright}$, ${}_{\trianglelefteq}$, ${}_{\trianglerighteq}$, ${}_{\origof}$, ${}_{\imageof}$, ${}_{\multimap}$, ${}_{\Join}$, ${}_{\backsimeq}$, ${}_{\Subset}$, ${}_{\Supset}$,
${}_{\pitchfork}$, ${}_{\lll}$, ${}_{\ggg}$, ${}_{\lesseqgtr}$, ${}_{\gtreqless}$, ${}_{\curlyeqprec}$, ${}_{\curlyeqsucc}$, ${}_{\npreceq}$, ${}_{\nsucceq}$, ${}_{\lnsim}$,
${}_{\gnsim}$, ${}_{\precnsim}$, ${}_{\succnsim}$, ${}_{\ntriangleleft}$, ${}_{\ntriangleright}$, ${}_{\ntrianglelefteq}$, ${}_{\ntrianglerighteq}$, ${}_{\frown}$, ${}_{\smile}$, ${}_{\vartriangle}$,
${}_{\blacktriangleright}$, ${}_{\blacktriangleleft}$, ${}_{\leqslant}$, ${}_{\geqslant}$, ${}_{\lessapprox}$, ${}_{\gtrapprox}$, ${}_{\lneq}$, ${}_{\gneq}$, ${}_{\lnapprox}$, ${}_{\gnapprox}$,
${}_{\lesseqqgtr}$, ${}_{\gtreqqless}$, ${}_{\eqslantless}$, ${}_{\eqslantgtr}$, ${}_{\preceq}$, ${}_{\succeq}$, ${}_{\precneqq}$, ${}_{\succneqq}$, ${}_{\precapprox}$, ${}_{\succapprox}$,
${}_{\precnapprox}$, ${}_{\succnapprox}$, ${}_{\subseteqq}$, ${}_{\supseteqq}$, ${}_{\subsetneqq}$, ${}_{\supsetneqq}$, ${}_{\nshortmid}$, ${}_{\nshortparallel}$, ${}_{\lvertneqq}$, ${}_{\gvertneqq}$,
${}_{\ngeqq}$, ${}_{\ngeqslant}$, ${}_{\nleqslant}$, ${}_{\nleqq}$, ${}_{\nsubseteqq}$, ${}_{\varsubsetneqq}$, ${}_{\nsupseteqq}$, ${}_{\varsupsetneqq}$, ${}_{\varsubsetneq}$, ${}_{\varsupsetneq}$,
${}_{\not}$

**Arrows.** ${}_{\gets}$, ${}_{\uparrow}$, ${}_{\to}$, ${}_{\downarrow}$, ${}_{\leftrightarrow}$, ${}_{\updownarrow}$, ${}_{\nwarrow}$, ${}_{\nearrow}$, ${}_{\searrow}$, ${}_{\swarrow}$,
${}_{\nleftarrow}$, ${}_{\nrightarrow}$, ${}_{\twoheadleftarrow}$, ${}_{\twoheadrightarrow}$, ${}_{\leftarrowtail}$, ${}_{\rightarrowtail}$, ${}_{\mapsto}$, ${}_{\hookleftarrow}$, ${}_{\hookrightarrow}$, ${}_{\looparrowleft}$,
${}_{\looparrowright}$, ${}_{\leftrightsquigarrow}$, ${}_{\nleftrightarrow}$, ${}_{\Lsh}$, ${}_{\Rsh}$, ${}_{\curvearrowleft}$, ${}_{\curvearrowright}$, ${}_{\circlearrowleft}$, ${}_{\circlearrowright}$, ${}_{\leftharpoonup}$,
${}_{\leftharpoondown}$, ${}_{\restriction}$, ${}_{\upharpoonleft}$, ${}_{\rightharpoonup}$, ${}_{\rightharpoondown}$, ${}_{\downharpoonright}$, ${}_{\downharpoonleft}$, ${}_{\rightleftarrows}$, ${}_{\leftrightarrows}$, ${}_{\leftleftarrows}$,
${}_{\upuparrows}$, ${}_{\rightrightarrows}$, ${}_{\downdownarrows}$, ${}_{\leftrightharpoons}$, ${}_{\rightleftharpoons}$, ${}_{\nLeftarrow}$, ${}_{\nLeftrightarrow}$, ${}_{\nRightarrow}$, ${}_{\Leftarrow}$, ${}_{\Uparrow}$,
${}_{\Rightarrow}$, ${}_{\Downarrow}$, ${}_{\Leftrightarrow}$, ${}_{\Updownarrow}$, ${}_{\Lleftarrow}$, ${}_{\Rrightarrow}$, ${}_{\leadsto}$, ${}_{\dashleftarrow}$, ${}_{\dashrightarrow}$, ${}_{\longleftarrow}$,
${}_{\longrightarrow}$, ${}_{\longleftrightarrow}$, ${}_{\Longleftarrow}$, ${}_{\Longrightarrow}$, ${}_{\Longleftrightarrow}$, ${}_{\longmapsto}$

**Large operators.** ${}_{\prod}$, ${}_{\coprod}$, ${}_{\sum}$, ${}_{\int}$, ${}_{\iint}$, ${}_{\iiint}$, ${}_{\oint}$, ${}_{\oiint}$, ${}_{\oiiint}$, ${}_{\bigwedge}$,
${}_{\bigvee}$, ${}_{\bigcap}$, ${}_{\bigcup}$, ${}_{\bigodot}$, ${}_{\bigoplus}$, ${}_{\bigotimes}$, ${}_{\biguplus}$, ${}_{\bigsqcup}$

**Symbols.** ${}_{\text{\textdollar}}$, ${}_{\text{\textasciicircum}}$, ${}_{\text{\textbar}}$, ${}_{\text{\textasciitilde}}$, ${}_{\pounds}$, ${}_{\yen}$, ${}_{\neg}$, ${}_{\circledR}$, ${}_{\degree}$, ${}_{\wp}$,
${}_{\mho}$, ${}_{\Game}$, ${}_{\forall}$, ${}_{\complement}$, ${}_{\partial}$, ${}_{\exists}$, ${}_{\nexists}$, ${}_{\emptyset}$, ${}_{\nabla}$, ${}_{\surd}$,
${}_{\infty}$, ${}_{\angle}$, ${}_{\measuredangle}$, ${}_{\sphericalangle}$, ${}_{\top}$, ${}_{\varvdots}$, ${}_{\circledS}$, ${}_{\diagup}$, ${}_{\diagdown}$, ${}_{\blacksquare}$,
${}_{\Box}$, ${}_{\blacktriangle}$, ${}_{\blacktriangledown}$, ${}_{\Diamond}$, ${}_{\bigstar}$, ${}_{\spadesuit}$, ${}_{\heartsuit}$, ${}_{\diamondsuit}$, ${}_{\clubsuit}$, ${}_{\flat}$,
${}_{\natural}$, ${}_{\sharp}$, ${}_{\checkmark}$, ${}_{\maltese}$, ${}_{\blacklozenge}$

**Letters.** ${}_{\text{\AE}}$, ${}_{\text{\O}}$, ${}_{\text{\ss}}$, ${}_{\text{\ae}}$, ${}_{\eth}$, ${}_{\text{\o}}$, ${}_{\text{\i}}$, ${}_{\text{\OE}}$, ${}_{\text{\oe}}$, ${}_{\text{\j}}$,
${}_{\Gamma}$, ${}_{\Delta}$, ${}_{\Theta}$, ${}_{\Lambda}$, ${}_{\Xi}$, ${}_{\Pi}$, ${}_{\Sigma}$, ${}_{\Upsilon}$, ${}_{\Phi}$, ${}_{\Psi}$,
${}_{\Omega}$, ${}_{\alpha}$, ${}_{\beta}$, ${}_{\gamma}$, ${}_{\delta}$, ${}_{\varepsilon}$, ${}_{\zeta}$, ${}_{\eta}$, ${}_{\theta}$, ${}_{\iota}$,
${}_{\kappa}$, ${}_{\lambda}$, ${}_{\mu}$, ${}_{\nu}$, ${}_{\xi}$, ${}_{\omicron}$, ${}_{\pi}$, ${}_{\rho}$, ${}_{\varsigma}$, ${}_{\sigma}$,
${}_{\tau}$, ${}_{\upsilon}$, ${}_{\varphi}$, ${}_{\chi}$, ${}_{\psi}$, ${}_{\omega}$, ${}_{\vartheta}$, ${}_{\phi}$, ${}_{\varpi}$, ${}_{\digamma}$,
${}_{\varkappa}$, ${}_{\varrho}$, ${}_{\epsilon}$, ${}_{\hbar}$, ${}_{\Im}$, ${}_{\ell}$, ${}_{\Re}$, ${}_{\Finv}$, ${}_{\aleph}$, ${}_{\beth}$,
${}_{\gimel}$, ${}_{\daleth}$, ${}_{\imath}$, ${}_{\jmath}$

**Delimiters.** ${}_{\lparen}$, ${}_{\rparen}$, ${}_{\lceil}$, ${}_{\rceil}$, ${}_{\lfloor}$, ${}_{\rfloor}$, ${}_{\lmoustache}$, ${}_{\rmoustache}$, ${}_{\ulcorner}$, ${}_{\urcorner}$,
${}_{\llcorner}$, ${}_{\lrcorner}$, ${}_{\langle}$, ${}_{\rangle}$, ${}_{\lgroup}$, ${}_{\rgroup}$

**Ellipses.** ${}_{\ldots}$, ${}_{\cdots}$, ${}_{\ddots}$

**Punctuation.** ${}_{\#}$, ${}_{\%}$, ${}_{\&}$, ${}_{\ldotp}$, ${}_{\lbrack}$, ${}_{\backslash}$, ${}_{\rbrack}$, ${}_{\_}$, ${}_{\{}$, ${}_{\}}$,
${}_{\S}$, ${}_{\P}$, ${}_{\text{\textendash}}$, ${}_{\text{\textemdash}}$, ${}_{\text{\textquoteleft}}$, ${}_{\text{\textquoteright}}$, ${}_{\text{\textquotedblleft}}$, ${}_{\text{\textquotedblright}}$, ${}_{\prime}$, ${}_{\backprime}$

**Accents.** ${}_{\ddot{n}}$, ${}_{\c{n}}$, ${}_{\^{n}}$, ${}_{\v{n}}$, ${}_{\={n}}$, ${}_{\'{n}}$, ${}_{\`{n}}$, ${}_{\u{n}}$, ${}_{\.{n}}$, ${}_{\r{n}}$,
${}_{\~{n}}$, ${}_{\H{n}}$, ${}_{\vec{n}}$

**Spacing.** The command ${}_{\ }$ draws no mark; it sets a space.

Beyond the table the slot takes any expression: an upright word, ${}_{\mathrm{ret}}$; a text string, ${}_{\text{word}}$; a nested index, ${}_{i_1}$; and the compound ${}_{\natural*}$ that the biquaternion articles use.

## Conventions of the Corpus Itself

The corpus has a small number of working conventions that are not mathematical.

**The menus.** Every article is registered in exactly one menu: `maths.md` for the mathematical corpus and `physics.md` for the physics corpus. An entry has the form of a link to the article followed by a comment that lists the contents of the article in outline. The mathematical menu opens with the category *Introduction and Conventions*, placed outside the parts. It has two subcategories: *Introduction to Mathematics*, which holds *Introduction to the Mathematical Corpus* and *AI Maths Review*, and *Conventions in Mathematics*, which holds this article and its six companions. An entry that begins with `+` is a **planned** article, one that is registered in the menu and not yet written; an entry without the marker has its article on disk.

**The groups inside a category.** A category of Parts I to IV lists its articles in four groups, each of which adds one thing to the group before it. The group `- Theory` holds the structure itself, read with the product of its elements. The group `- Operator Theory` holds the operators on that structure — the left and right multiplications, the derivations, the automorphisms, the actions and the sandwich — and adds an operator layer and nothing else. The group `- * Theory` holds the same structure read with an involution on its **elements**. The group `- * Operator Theory` holds the operators built from the **involution**, of which the adjoint is the archetype. The front-matter category *Introduction and Conventions* is the exception: it lists two subcategories and no group.

**The two involutions.** The star names the involutive layer in both groups, and the layer of the elements and the layer of the operators are two structures and not one: the involution of `- * Theory` sits on the elements and the adjoint of `- * Operator Theory` sits on the operators. They need not coincide: an involution on the elements does not by itself produce an adjoint on the operators, and two adjoints of the same structure may differ — the transpose and the Hermitian adjoint of a matrix are both adjoints, taken with respect to different pairings. When the two do agree the representation is a `*`-representation, and the agreement is proved in the article, never assumed by the menu.

**The order and the fill rule.** The four groups are placed in the order above, and the group `- Applications`, which holds the concrete instances of the structure, closes the category. The groups `- Operator Theory` and `- * Operator Theory` are present in a category whenever it has an operator layer, and the group `- * Theory` is present in every category of Parts I to IV, whether or not it yet holds an article.

**The category names and numbers.** The menu numbers its categories, and an article elsewhere in the corpus may address one by number rather than by name: *category n* means the n-th category of Parts I to VI, read in order, the front matter *Introduction and Conventions* not being counted. This article refers to categories by **name** throughout, because the names are the stable thing and the numbers shift whenever a category is inserted or split. A reader who meets a bare number in another article can resolve it in the menu.

**The article files.** The corpus is split into two collections, each with its own folder: a mathematical article is a file `articles_maths/<slug>.md` and a physical article is a file `articles_physics/<slug>.md`, where the slug is the title in lower case with hyphens in place of spaces and punctuation. The folder and the menu agree — an article lies in the folder whose menu lists it, and no article lies in both.

**The article skeleton.** Every article opens with its title as the first heading, followed by an *Introduction* that states what the article does and what it assumes, then the thematic sections, and closes with three sections in this order: *Summary*, *Summary of Notation*, and *Further Reading*. The introduction states the article's boundaries — what it deliberately does not cover, and where the reader will find it. This article is the one exception: its notation is merged into the Summary and its table closes the article.

**Cross-references and boundaries.** A concept is introduced once, in the category that owns it, and referred to afterwards rather than restated. Articles do not duplicate the content of other articles; they cite them. Every article that touches a structure belonging to a later part states the deferral explicitly, which is the mechanism by which Rule 1 is enforced.

**The word "interval".** Two different objects share the word, and the corpus keeps them apart. In the mathematical corpus an **interval** is an order-theoretic or lattice object: a convex subset of a linearly ordered set, the interval $[a,b]=\{x:a\le x\le b\}$ of a lattice or of a poset of effects, defined by the order and not by a form. In the physical corpus the **interval** is the value of the quadratic form, $\langle\tilde Q\rangle_{\natural}=-\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ on the material sector, defined by the form and not by an order. A statement about the sign of the interval is therefore never a statement about a lattice interval, and a lattice interval is never the line element; where the two senses could meet, the corpus writes *the form value* or *the quadratic form* for the physical one.

## LaTeX and Typesetting

The articles are rendered with KaTeX on the page, and the following rules are observed in the source.

- Inline mathematics is written between single dollars, and display mathematics between double dollars on lines of their own.
- Inline mathematics never spans a line break. If a formula is too long, it is displayed.
- Display mathematics inside a list is indented four spaces.
- A prime may follow a subscript as well as precede it: the forms `q'_t` and `q_t'` are both admitted, and an article keeps one order throughout.
- Tables are Markdown tables. A LaTeX array is never used for a table.
- Every heading that introduces a comparison or a classification is a real `###` heading, and the objects are defined before they are tabulated.
- **Bold marks the result.** In a Remark that states a verdict, the clause carrying the outcome is
  set in bold, `**...**`, the object of the sentence staying in plain roman: *the subspace **is a
  commutative Jordan algebra over $\mathbb{R}$ of degree two***. A statement already displayed as a
  Theorem, a Proposition or a Proof is not bolded; the convention applies to the prose of a Remark and
  to the lead sentence of a section that states an outcome.
- The third derivative is written `d^3/dt^3`, and the macro `\slashed` is available. The characters `|`, `{`, `}`, `<` and `>` inside mathematics need no escaping.
- A malformed formula is rendered in red on the page rather than reported as an error, so mathematics is checked by eye and not by the absence of a warning.

## Summary

Two **superscript tokens** run beside the marks of the elements: $\mathrm{fop}$ marks a Fock operator, an operator on the Fock space and not an element of the algebra, and $\mathrm{opp}$ marks the opposite algebra, whose product is reversed. The two are not read for one another: $\mathrm{fop}$ is written on a glyph, $\mathrm{opp}$ on an algebra name. The Fock mark combines with the dagger, the mark first, $a^{\mathrm{fop}\dagger}$, and the dagger alone never marks a glyph as an operator. Two further upright superscripts, $\mathrm{fn}$ on a function and $\mathrm{spin}$ on a group element, name objects outside the algebra.

A **subscript** is written with the underscore and takes a single token: one character bare, two or more in braces. It counts when it only distinguishes occurrences and names when it is a role label; a role-labelled element carries its label in its coefficients. The admitted forms are a digit, a letter, two indices, a sign, an upright word and a grouped expression, and the slot takes any KaTeX expression beyond them. A subscript is never a partial derivative.

The **working conventions of the corpus** are these. Every article is registered in exactly one menu, `maths.md` or `physics.md`, with a comment that outlines it, and a leading `+` marks a planned article. A category of Parts I to IV lists its articles in the four groups Theory, Operator Theory, `*` Theory and `*` Operator Theory, and `- Applications` closes it. The article files are `articles_maths/<slug>.md` and `articles_physics/<slug>.md`, and every article follows the skeleton Introduction, thematic sections, Summary, Summary of Notation, Further Reading.

The **category numbers** count the categories of the parts in menu order; the front matter is not counted. Since a number shifts when a category is inserted or split, an article addresses a category by name, and the name is the stable thing. The **typography** is KaTeX on the page: inline mathematics between single dollars and never across a line break, display mathematics between double dollars on lines of their own, tables in Markdown and never as a LaTeX array, and a malformed formula rendered in red rather than reported.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $^{\mathrm{fop}}$ | A Fock operator, an operator on the Fock space and not an element of the algebra |
| $^{\mathrm{opp}}$ | The opposite algebra, the algebra with the reversed product |
| $^{\mathrm{fn}}$ | A function from a domain into the algebra |
| $^{\mathrm{spin}}$ | An element of $\mathrm{Spin}(n)$ or $\mathrm{Pin}(n)$ on a principal bundle |
| `- Theory`, `- Operator Theory`, `- * Theory`, `- * Operator Theory` | The four groups of a category, in that order |
| `- Applications` | The group that closes a category with the concrete instances of its structure |
| `+` | A planned article, registered in the menu and not yet written |
| `articles_maths/<slug>.md` | The file of a mathematical article; the slug is the title in lower case with hyphens |
| Introduction, thematic sections, Summary, Summary of Notation, Further Reading | The skeleton of every article |

## Further Reading

- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for a notation fixed once and used without variation.
- Donald E. Knuth, *The TeXbook* (Addison-Wesley, 1984). The typographic conventions the source of the corpus follows.
