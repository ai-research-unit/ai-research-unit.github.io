# __Conventions in Mathematics__

## Introduction

This article gathers the conventions the mathematical articles assume: the symbols, the arithmetic conventions, the shape of a generic element and its coefficients, the marks reserved for the conjugations of an algebra with an involution and for the adjoint of an operator, the convention of the form and the norm, the typographic rules of the source, and the working conventions of the corpus itself — the menu, the groups inside a category, the article files and the skeleton.

They are stated once, here, so that no other article need repeat them. This article states conventions only: the proofs and the properties of the objects it names belong to the articles cited beside them. How the articles are organised into the six parts and their categories is the subject of the companion article *Introduction to Mathematics*; this one is the reference for the elements, the marks, the glyphs and the layout.

## Notational Conventions

The conventions below are those used throughout the corpus.

### Symbols

| Symbol | Meaning |
|---|---|
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ | The naturals, integers, rationals, reals, complex numbers |
| $\mathbb{D}$ | The split-complex numbers, $\mathbb{R}[x]/(x^2-1)$ |
| $\mathbb{D}'$ | The dual numbers, $\mathbb{R}[x]/(x^2)$ |
| $\mathbb{H}$ | The real quaternions |
| $\mathbb{H}_{\mathrm{s}}$ | The split-quaternions, $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ |
| $\mathbb{B}_{\mathrm{r}}$ | The reduced biquaternions, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \oplus \mathbb{C}$, equivalently the tessarines or the double-complex numbers |
| $\mathbb{B}$ | The biquaternions, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\mathbb{H}_{\mathbb{D}}$ | The split-biquaternions, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $\mathbb{O}$ | The octonions |
| $G$ | A group; $R$ a ring; $k$, $F$ a field; $V$ a vector space; $M$ a module; $A$ an algebra |
| $\mathrm{G}, \mathrm{H}, \mathrm{SL}_n$ | Lie algebras |
| $\mathrm{M}, \mathrm{P}$ | Ideals and prime ideals |
| $\operatorname{Sym}(X), \operatorname{Aut}(X)$ | Symmetric group of a set; automorphism group of a structure |
| $\operatorname{End}(V), \operatorname{Der}(A), \operatorname{Inn}(A), \operatorname{Out}(A)$ | Endomorphisms, derivations, inner and outer automorphisms |
| $GL, SL, PGL, O, SO, U, SU, Sp$ | The classical groups |
| $T(V), S(V), \Lambda(V), Cl(V,Q)$ | Tensor, symmetric, exterior and Clifford algebras |
| $V^{\otimes n}, S^n V, \Lambda^n V$ | Tensor, symmetric and exterior powers |
| $\langle v,w\rangle, Q(v), \lVert x\rVert$ | Bilinear form, quadratic form, norm |
| $\bullet$ | The symmetrised (Jordan) product, $x \bullet y = \tfrac{1}{2}(xy + yx)$; the circle $\circ$ is reserved for the composition of maps |
| $\bar{\cdot}, {}^{\natural}, {}^{*}, {}^{\flat}, {}^{\dagger}$ | The conjugations of an algebra with an involution, and the adjoint of an operator; *The Conjugations and the Adjoint* below fixes their meanings |
| $\tilde\Pi$, $\tilde\pi$, $\Pi$ | An idempotent or a pure state, and the minimal left ideal it generates; the biquaternion layer writes $\tilde\Pi$, the quaternion layer $\tilde\pi$, and the tilde-free layers $\Pi$ (§*The Idempotent Convention*) |
| $\tilde\Xi$, $\tilde\xi$, $\Xi$ | A root of $1$: the biquaternion layer writes $\tilde\Xi$, the quaternion layer $\tilde\xi$, and the tilde-free layers $\Xi$ (§*The Root Convention*) |
| $\tilde P, \tilde q, \tilde Q$ | A generic element of the algebra: the quaternion, split-quaternion, biquaternion or split-biquaternion one |
| $\hat q, \hat Q$ | A pure element, an element with no scalar part: the quaternion and split-quaternion layers write $\hat q$, the biquaternion and split-biquaternion layers $\hat Q$ (§*Pure Elements and their Coefficients*) |
| $\hat u$ | A unit pure quaternion, the axis of a rotation |
| $\hat U$ | A unit pure biquaternion, of norm one |
| $\hat\Xi$ | A pure root of $1$ of the biquaternion or split-biquaternion layer |
| $\hat\Upsilon$ | A pure nilpotent of the biquaternion or split-biquaternion layer |

### Groups, Rings and Operations

A group is written multiplicatively by default, with unit $e$ and inverse $x^{-1}$, and additively when it is the underlying group of a ring, with zero $0$ and inverse $-x$. A ring is a triple $(R, +, \cdot)$; a ring need not be commutative and need not have a unit, and the article that introduces it says which conventions it adopts. A field is a commutative ring with $1 \neq 0$ in which every nonzero element is invertible. A module is written with its scalars on the left unless the article says otherwise, and the side matters as soon as the ring is non-commutative. Products are written by juxtaposition: $ab$ for the product in a group or an algebra, $fv$ for the action of a scalar on a vector. The **symmetrised (Jordan) product** is written with a bullet, $x \bullet y = \tfrac{1}{2}(xy + yx)$, and the circle $\circ$ is kept for the **composition of maps**, as in $\mathrm{H}_{\tilde Q}\circ\mathrm{H}_{\tilde R}$.

### LaTeX and Typesetting

The articles are rendered with KaTeX on the page, and the following rules are observed in the source.

- Inline mathematics is written between single dollars, and display mathematics between double dollars on lines of their own.
- Inline mathematics never spans a line break. If a formula is too long, it is displayed.
- Display mathematics inside a list is indented four spaces.
- A prime may follow a subscript as well as precede it: the forms `q'_0` and `q_0'` are both admitted, and an article keeps one order throughout.
- Tables are Markdown tables. A LaTeX array is never used for a table.
- Every heading that introduces a comparison or a classification is a real `###` heading, and the objects are defined before they are tabulated.
- **Bold marks the result.** In a Remark that states a verdict, the clause carrying the outcome is
  set in bold, `**...**`, the object of the sentence staying in plain roman: *the subspace **is a
  commutative Jordan algebra over $\mathbb{R}$ of degree two***. A statement already displayed as a
  Theorem, a Proposition or a Proof is not bolded; the convention applies to the prose of a Remark and
  to the lead sentence of a section that states an outcome.
- The macros `\dddot` and `\slashed` are available. The characters `|`, `{`, `}`, `<` and `>` inside mathematics need no escaping.
- A malformed formula is rendered in red on the page rather than reported as an error, so mathematics is checked by eye and not by the absence of a warning.

## The Elements and their Coefficients

The case and the tilde of the glyph are fixed first, and the element is written after. A generic element is preferably written so that the glyph alone identifies its algebra, two features being read together: the **case** separates a real scalar from a complex one, and a **tilde** marks the quaternionic factor.

| System | Name | Generic element | Scalar–vector decomposition | Coefficients |
|---|---|---|---|---|
| $\mathbf{2}$ | Booleans | $\alpha, \beta, \dots$ | — | — |
| $\mathbb{N}$ | Naturals | $n, m, \dots$ | — | — |
| $\mathbb{Z}$ | Integers | $n, m, \dots$ | — | — |
| $\mathbb{Q}$ | Rationals | $a, b, c, \dots$ | — | — |
| $\mathbb{R}$ | Reals | $a, b, c$ | — | — |
| $\mathbb{C}$ | Complex numbers | $A = a + ia'$, $B = b + ib'$ | Scalar $a$, vector $ia'$ | Real, $a, a'$ |
| $\mathbb{D}$ | Split-complex numbers | $A = a + ja'$, $B = b + jb'$ | Scalar $a$, vector $ja'$ | Real, $a, a'$ |
| $\mathbb{D}'$ | Dual numbers | $A = a + \varepsilon a'$, $B = b + \varepsilon b'$ | Scalar $a$, vector $\varepsilon a'$ | Real, $a, a'$ |
| $\mathbb{H}$ | Quaternions | $\tilde q = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$ | $q_0e_0 + \vec q$, $\vec q = q_1e_1 + q_2e_2 + q_3e_3$ | Real, $q_\mu$ |
| $\mathbb{H}_{\mathrm{s}}$ | Split-quaternions | $\tilde q = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$ | $q_0e_0 + \vec q$, $\vec q = q_1e_1 + q_2e_2 + q_3e_3$ | Real, $q_\mu$ |
| $\mathbb{B}_{\mathrm{r}}$ | Reduced biquaternions | $T = A + Bj$ | Scalar $A$, vector $Bj$ | Complex, $A = a + ia'$, $B = b + ib'$ |
| $\mathbb{B}$ | Biquaternions | $\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ | $Q_0e_0 + \vec Q$, $\vec Q = Q_1e_1 + Q_2e_2 + Q_3e_3$, $Q_\mu\in\mathbb{C}$ | Complex, $Q_\mu = q_\mu + iq'_\mu$ |
| $\mathbb{H}_{\mathbb{D}}$ | Split-biquaternions | $\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ | $Q_0e_0 + \vec Q$, $\vec Q = Q_1e_1 + Q_2e_2 + Q_3e_3$, $Q_\mu\in\mathbb{D}$ | Split-complex, $Q_\mu = q_\mu + jq'_\mu$ |
| $\mathbb{O}$ | Octonions | $o = o_0e_0 + o_1e_1 + \cdots + o_7e_7$ | $o_0e_0 + \vec o$, $\vec o = o_1e_1 + \cdots + o_7e_7$ | Real, $o_\mu$ |

Five rules are read off the table. **A complex element carries a majuscule**, $A$ or $B$, the case naming the scalar sector: an upper-case glyph has a scalar sector larger than the reals, a lower-case one has the reals. **The second coordinate of a complex element carries a prime**, $A = a + ia'$, with $j$ in place of $i$ for the split-complex numbers and $\varepsilon$ for the dual numbers. **The four quaternionic elements carry a tilde**: lower case for the quaternions and the split-quaternions, $\tilde q$, and upper case for the biquaternions and the split-biquaternions, $\tilde Q$. The reduced biquaternion element carries **no tilde**: its algebra has no quaternionic factor, being the commutative two-parameter system over the complex scalars, and it is written $T = A + Bj$ with the two complex coordinates $A = a + ia'$ and $B = b + ib'$, the second unit $j$ being the hyperbolic unit of the corpus, $j^{2} = +1$ and $ji = ij$, so that the basis is $1, i, j, ij$. **The octonion element carries no tilde either**, $o = o_0e_0 + \cdots + o_7e_7$: the octonions have no quaternionic factor, so the tilde is carried by the four quaternionic elements alone. And **the arithmetic systems and the reals carry a letter that is theirs alone**: $\alpha, \beta$ the Booleans, $n, m$ the naturals and the integers, and $a, b, c$ the rationals and the reals — a letter, no prime, no tilde, no coefficient sector, since these elements are not written as linear combinations. Finally, **the element is a scalar part plus a vector part**: the scalar part is carried by the unit — $1$ in the commutative two-parameter systems, $e_0$ in the quaternionic and octonionic ones — and the vector part by the remaining basis directions, carrying the arrow, $\vec q$, $\vec Q$ or $\vec o$, so that $\tilde Q = Q_0e_0 + \vec Q$ is written in the coefficients according to the system; the two are the fixed and the anti-fixed spaces of the intrinsic conjugate, and the arithmetic systems, which are not written as linear combinations, have no vector part. The arrow is reserved for the vector part of a named element, and the hat for a pure element, one with no scalar part (§*Pure Elements and their Coefficients*): the vector part of $\tilde Q$ is $\vec Q$, a pure element standing by itself is $\hat q$ or $\hat Q$, and a unit pure quaternion is written $\hat u$. The two marks are never stacked.

For the biquaternions, whose basis is $e_0, e_1, e_2, e_3$ with $e_0 = 1$ the unit,

$$
\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3, \qquad Q_\mu = q_\mu + iq'_\mu,
$$

where the four coefficients $Q_\mu$ are complex, and each of them splits into a real part $q_\mu$ and an imaginary part $q'_\mu$. **The two parts of a coefficient share its letter**, the imaginary part carrying a prime. The shape is the same in the quaternion systems; only the coefficient sector changes, and the table above gives the element and the coefficients of each system. The unit $e_0$ is the identity in the two quaternion systems, and the real and the imaginary part of a coefficient may be read off only where the scalar sector is larger than the reals, which is the case in $\mathbb{C}$ and $\mathbb{B}$ and not in $\mathbb{R}$ or $\mathbb{H}$.

The case and the tilde are read independently, and the glyph of a generic element is the two together: $a$ is real, $A$ complex, split-complex or dual, $T$ reduced biquaternion — upper case, no tilde, and two complex coordinates — $\tilde q$ quaternion or split-quaternion, $\tilde Q$ biquaternion or split-biquaternion, and $o$ octonion.

**The generic element is written $\tilde{P}$ or $\tilde{Q}$.** A statement that holds for every element is written with $\tilde P$ — the trace pairing $\operatorname{Tr}(\tilde P\tilde Q) = 2\operatorname{Sc}(\tilde P\tilde Q)$, the commutator bracket $[\tilde P, \tilde Q] = \tilde P\tilde Q - \tilde Q\tilde P$, the general plain bilinear form $\langle\tilde P, \tilde Q\rangle$ and the multiplicativity $\langle\tilde P\tilde Q\rangle_{\natural} = \langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$ — inherited from *Idempotents of the General Plain Algebra* and its companions, which write the generic element $\tilde P$ beside the idempotent $\tilde\Pi$.

**The coordinates carry the letter of the element.** The components of a generic element are written with the same letter as the element and a subscript: $q_\mu$ for $\tilde q$, $Q_\mu = q_\mu + iq'_\mu$ for $\tilde Q$, and $o_\mu$ for $o$; a Euclidean vector part assembled from the non-scalar components carries the arrow, $\vec q$, $\vec Q$ or $\vec o$; and a plain real variable is $a$, $b$ or $c$. In the synthetic studies of Part VI the letters $x, y$ and $z$ name neither an element nor a coordinate of any system: they appear there only as a formal indeterminate, as in $\mathbb{R}[x]/(x^2-1)$, or inside the name of an operator, a map or a function that the article itself defines.

**It is allowed to add subscripts when several elements of the same kind are used.** Where a statement carries more than one generic element, the occurrences are told apart by a subscript, $\tilde Q_1, \tilde Q_2, \dots$, and a second family in the same statement takes the next numbers.

This is a **preferred convention** — a preference, not a strict rule, not to be enforced by rewriting other articles: the basis $e_0, \dots, e_3$, the central unit $i$, the Euclidean vector $\vec q$, the coefficients $q_\mu, q'_\mu$, indices such as $\mu, \nu, k$, structure constants, and the individual elements an article defines keep the symbols that article gives them. Where the constructions that share a glyph must be told apart — the complex from the split-complex and the dual, the quaternion from the split-quaternion, the biquaternion from the split-biquaternion — the glyph is qualified by a subscript, as in $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{H}_{\mathbb{D}}$.












### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |
| The reduced $K$-theory group | $\tilde K^0$ | $K^0_{\mathrm{red}}$ |
| A lift of a path or a section | $\tilde\gamma$, $\tilde\sigma$ | $\gamma^{\mathrm{lift}}$, $\sigma^{\mathrm{lift}}$ |
| The reduced $K$-theory group | $\tilde K^0$ | $K^0_{\mathrm{red}}$ |
| The reduced homology of a space | $\tilde H_n(X)$ | $H^{\mathrm{red}}_n(X)$ |
| The reduced Euler characteristic | $\tilde\chi(X)$ | $\chi^{\mathrm{red}}(X)$ |
| A reduced cohomology theory | $\tilde E^k(X)$ | $E^{k,\mathrm{red}}(X)$ |
| The ordered Čech complex | $\tilde C^p$ | $C^p_{\mathrm{ord}}$ |
| A lift of a path or a section | $\tilde\gamma$, $\tilde\sigma$ | $\gamma^{\mathrm{lift}}$, $\sigma^{\mathrm{lift}}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.












### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.











### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.










### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.









### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.








### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.







### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.






### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.





### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.




### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.



### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $x^{\mathrm{lift}}$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.


### The Tilde and the Other Fields

The tilde is the mark of the quaternionic factor here, and that reading of the accent is peculiar to this corpus. In the rest of mathematics the same accent marks several unrelated objects, and the table below gives the object, its customary glyph, and the glyph written here when the object occurs beside an element of the algebra. **The rule is that the tilde is never borrowed**: an object of the list occurring in an article of the corpus is written with the qualifier of the third column.

| Object | Customary glyph | Written here as |
|---|---|---|
| The reverse of a multivector, in geometric algebra | $\tilde A$ | $A^{\mathrm{rev}}$ |
| The quaternion conjugate, in the older quaternion literature | $\tilde q$ | $\tilde q^{\natural}$ |
| A universal cover, $\tilde X \to X$ | $\tilde X$ | $X^{\mathrm{cov}}$ |
| A lift of $x$ | $\tilde x$ | $\ell(x)$ |
| The sheaf attached to a module | $\tilde M$ | $M^{\mathrm{sh}}$ |
| A normalisation | $\tilde X$ | $X^{\mathrm{norm}}$ |
| The Fourier transform of $f$ | $\tilde f(\omega)$ | $f^{\wedge}(\omega)$ |
| The reflection of a function, $\mathcal F^2$ | $\tilde f$ | $f^{\mathrm{refl}}$ |
| A contragredient representation | $\tilde\pi$ | $\pi^{\vee}$ |
| The dual group | $\tilde G$ | $G^{\vee}$ |
| The sample median | $\tilde x$ | $\operatorname{med}(x)$ |
| An estimator | $\tilde\theta$ | $\theta^{\mathrm{est}}$ |
| A kernel density | $\tilde f$ | $f^{\mathrm{ker}}$ |
| A computed or approximate value | $\tilde x$ | $x^{\mathrm{num}}$ |
| A nondimensionalised variable | $\tilde t = t/t_0$ | the ratio $t/t_0$ itself |
| A comparison manifold, metric, curvature | $\tilde M, \tilde g, \tilde K$ | $M_c, g_c, K_c$ |
| An affine Dynkin or Coxeter type | $\tilde A_n$ | $A_n^{(1)}$ |

**The sharpest of the list is the reverse of geometric algebra**, because the field is a neighbour of this one: there the tilde is the reverse, whereas here the reverse is the natural sign, $\tilde Q^{\natural}$, and the other two accents of that field are taken as well, the bar by coefficientwise conjugation, $\bar Q$, and the hat by purity, $\hat Q$. **No mark of this convention is borrowed by the third column**: an entry qualifies the usual letter, as $M^{\mathrm{sh}}$ and $f^{\wedge}$ do, or takes a letter the algebra leaves free, as $\operatorname{med}$ does, and a quantity with no settled glyph is written out, as the ratio $t/t_0$.


## Pure Elements and their Coefficients

A **pure element** is an element with no scalar part. In the quaternion and biquaternion layers the scalar part is carried by $e_0$, so a pure element is one whose $e_0$-coefficient vanishes and which is carried by the three vector directions alone. The pure elements of a layer are exactly the elements of its **vector subspace** $\mathrm{Vect}$, the anti-fixed space of the intrinsic conjugate,

$$
\hat q^{\natural} = -\hat q, \qquad \hat Q^{\natural} = -\hat Q,
$$

so a pure real quaternion is a vector of $\mathbb{R}^{3}$ and a pure biquaternion an element of a complex vector space of real dimension six.

**The glyph drops the tilde and carries the hat.** The tilde marks the quaternionic factor of an element that is read with its scalar part beside its vector part; a pure element is read on its vector part alone, so it is written with the hat and without the tilde, $\hat q$ in the quaternion and split-quaternion layers and $\hat Q$ in the biquaternion and split-biquaternion ones. The case is unchanged, and the hat is the only mark: a pure element is never written with a tilde, and it is never written with the arrow, which belongs to the vector part of a named element.

**The hat is reserved for pure elements.** Three rules follow from this. First, **the hat marks a pure element and nothing else**: an element with a nonzero scalar part is never written with a hat, whatever its magnitude or its role. Second, **a unit element carries the hat only if it is pure**: the unit pure quaternion $\hat u$ and the unit pure biquaternion $\hat U$ carry it, whereas a unit element that has a scalar part — a rotor $\tilde q$ of unit norm, say — carries no hat, its unit length being carried by the construction that names it. Third, **a unit in the direction of an element takes that element as a subscript**, written $\hat u_{e}$ as in $\hat u_B$ for the unit along the field $B$; the subscript names the element whose direction is taken, and the hat on $\hat u$ records that the unit is pure.

| System | Name | Pure element | Pure unit element | Scalar part | Coefficients |
|---|---|---|---|---|---|
| $\mathbb{H}$ | Quaternions | $\hat q = q_1e_1 + q_2e_2 + q_3e_3$ | $\hat u$ | $q_0 = 0$ | Real, $q_\mu$ |
| $\mathbb{H}_{\mathrm{s}}$ | Split-quaternions | $\hat q = q_1e_1 + q_2e_2 + q_3e_3$ | $\hat u$ | $q_0 = 0$ | Real, $q_\mu$ |
| $\mathbb{B}$ | Biquaternions | $\hat Q = Q_1e_1 + Q_2e_2 + Q_3e_3$ | $\hat U$ | $Q_0 = 0$ | Complex, $Q_\mu = q_\mu + iq'_\mu$ |
| $\mathbb{H}_{\mathbb{D}}$ | Split-biquaternions | $\hat Q = Q_1e_1 + Q_2e_2 + Q_3e_3$ | $\hat U$ | $Q_0 = 0$ | Split-complex, $Q_\mu = q_\mu + jq'_\mu$ |

Three rules are read off the table. **A pure element is the vector part of an element read on its own.** For $\tilde q = q_0e_0 + \vec q$ the vector part $\vec q$ is a pure quaternion, and for $\tilde Q = Q_0e_0 + \vec Q$ the vector part $\vec Q$ is a pure biquaternion; the difference between $\vec q$ and $\hat q$ is one of role alone, the arrow naming the part inside the split of a named element and the hat naming a pure element that stands by itself. **A pure element is anti-fixed by the intrinsic conjugate**, $\hat q^{\natural} = -\hat q$, having no scalar part to be fixed. **The hat marks purity, not magnitude.** A pure element is of arbitrary magnitude; a unit pure element — a unit pure quaternion $\hat u$ — carries no second mark, its unit length being carried by the construction.

**The pure glyphs.** The hat is laid on the glyph of a special element on the same case rule that governs the layer: the pure root is $\hat\Xi$ in the biquaternion and split-biquaternion layers and $\hat\xi$ in the quaternion and split-quaternion ones, and the pure nilpotent is $\hat\Upsilon$ in the biquaternion and split-biquaternion layers and $\hat\nu$ in the quaternion and split-quaternion ones.

**The hat has priority over the tilde.** Where an element is pure, the hat is written whatever else the element is, and the tilde of a special glyph is dropped: a pure root is $\hat\Xi$ and a pure nilpotent is $\hat\Upsilon$ (or $\hat\xi$ and $\hat\nu$ in the quaternion layers), never $\tilde\Xi$ or $\tilde\Upsilon$. The tilde belongs to the general element, read with its scalar part beside its vector part, and a pure element has no scalar part to be read against; purity therefore decides the mark. The special conventions that write the root $\tilde\Xi$ or the nilpotent $\tilde\Upsilon$ name the **general** element of that class, which need not be pure, and an element that is at once special and pure is written with the hat and only the hat.

A pure glyph is given from the quaternions to the biquaternions only. The layers with no quaternionic factor have no intrinsic conjugate to take a vector part against, and the commutative two-parameter systems carry their imaginary part in a single coefficient, $A = a + ia'$; the pure elements of the octonion layer are deferred with the layer.

## The Conjugations and the Adjoint

The biquaternion algebra carries four natural involutions, all of them used in the series, together with the adjoint of an operator, which belongs to the operators and not to the algebra:

| Map | Mark | What it is |
|---|---|---|
| Complex conjugation | $\bar{\cdot}$ | The involution of the base, extended to the element |
| Quaternion conjugation | ${}^{\natural}$ | The intrinsic conjugate: it fixes the scalars and negates the vectors |
| Hermitian conjugation | ${}^{*}$ | The involution of the algebra, $\bar{\cdot}\circ{}^{\natural}$ |
| Anti-Hermitian conjugation | ${}^{\flat} = -{}^{*}$ | The negative of the star |
| Operator adjoint | ${}^{\dagger}$ | The general adjoint of an operator, $(L_a)^{\dagger} = L_{a^{*}}$ |

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

## The Special Elements: Root, Idempotent and Nilpotent

### The Root Convention

The roots carry a symbol of their own, beside the idempotent $\tilde\Pi$ (§*The Idempotent Convention*) and the nilpotent $\tilde\nu$ (§*The Nilpotent Convention*): the **xi**, in the two cases.

A **root of $1$** of the algebra is an element $\tilde\Xi$ with $\tilde\Xi^2 = 1$. More generally a **root of a central value** $\lambda$ is an element with $\tilde\Xi^2 = \lambda e_0$; the roots of the three central values $-1, 0, +1$ are determined in *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general problem is *Square Roots of a General Element in the Biquaternion Algebra*.

**The square is read in a named product**, the algebra product unless the statement names another, as for the nilpotents: the class is relative to the product, and the roots of a value are read product by product in *Square Roots of a General Element in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*.

**The case rule splits the glyph, as it does for the elements, the idempotents and the nilpotents.** The roots of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde\Xi$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde\xi$; and those of the complex, split-complex, dual and reduced biquaternion layers carry the plain capital, $\Xi$, no tilde being written where there is no quaternionic factor.

**The coordinates carry the letter of the root**, as for a general element: in $\mathbb{B}$ the root is $\tilde\Xi = \Xi_0e_0 + \Xi_1e_1 + \Xi_2e_2 + \Xi_3e_3$ with $\Xi_\mu = \xi_\mu + i\xi'_\mu$, its scalar part $\Xi_0$ and its vector part $\vec\Xi = \vec\xi + i\vec\xi'$; in $\mathbb{H}$ it is $\tilde\xi = \xi_0e_0 + \xi_1e_1 + \xi_2e_2 + \xi_3e_3$ with real $\xi_\mu$.

**It is allowed to add subscripts when several roots are used.** **The subscript of a root is numeric when it counts and a role label when it names.** Where more than one occurs the roots are numbered, $\tilde\Xi_1, \tilde\Xi_2$, as for the nilpotents and for the idempotent pairs other than the complete sign pair of §*The Idempotent Convention*; where a root plays a named role, it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The root glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde\Xi$ | A root of $1$ of the biquaternion or split-biquaternion layer |
| $\tilde\xi$ | A root of $1$ of the quaternion or split-quaternion layer |
| $\Xi$ | A root of $1$ of the complex, split-complex, dual or reduced biquaternion layer, where no tilde is written |

The convention is one of **notation, not of substance**: an element written $\tilde\Xi$ is not a different kind of object from one written $\tilde Q$, only an element known to be a root of $1$.

### The Idempotent Convention

The convention of *The Elements and their Coefficients* fixes the case and the tilde of a generic element. The idempotents carry a symbol of their own, and the corpus uses it throughout.

An **idempotent** of the algebra is an element $\tilde\Pi$ with $\tilde\Pi^2 = \tilde\Pi$, and a **projector** is an idempotent operator, $p^2 = p$, that is an idempotent of the morphism space, not an element of the algebra; the two are different objects, and an idempotent element corresponds to a projector when its multiplication operator is idempotent. An idempotent fixed by the star, $\tilde\Pi^{*} = \tilde\Pi$, is a **Hermitian idempotent**, and the rank-one Hermitian idempotents of $\mathbb{M}_+$, the Hermitian subspace, are the **pure states**.

**The case rule splits the glyph, as it does for the elements.** The idempotents of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde\Pi$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde\pi$; and those of the complex, split-complex, dual and reduced biquaternion layers carry the plain capital, $\Pi$, no tilde being written where there is no quaternionic factor. The same splitting of the identity is written $\tilde\pi_{1,2}$ in $\mathbb{H}_{\mathrm{s}}$ (*Split-Quaternion Idempotents and Projections*) and $\Pi_{1,2}$ in $\mathbb{D}$ (*Split-Complex Idempotents and Projections*), the same $\Pi_{1,2}=\tfrac12(1\pm j)$ in the reduced biquaternion layer $\mathbb{B}_{\mathrm{r}}$, and the idempotents of the split-biquaternion layer are the $\tilde\Pi_{1,2}$ of *Split-Biquaternion Idempotents and Projections*; the layer fixes the glyph.

The involution here is the star on the elements, as *The Conjugations and the Adjoint* fixes it, and *Conventions in the Biquaternion Universe* writes the same involution with the same star, $\tilde\Pi^{*} = \tilde\Pi$: the two corpora agree on the mark, and it is the dagger that is confined to the operators.

**The coordinates carry the letter of the idempotent**, as for a general element: in $\mathbb{B}$ the idempotent is $\tilde\Pi = \Pi_0e_0 + \Pi_1e_1 + \Pi_2e_2 + \Pi_3e_3$ with $\Pi_\mu = \pi_\mu + i\pi'_\mu$, its scalar part $\Pi_0$ and its vector part $\vec\Pi = \vec\pi + i\vec\pi'$; in $\mathbb{H}$ it is $\tilde\pi = \pi_0e_0 + \pi_1e_1 + \pi_2e_2 + \pi_3e_3$ with real $\pi_\mu$.

**It is allowed to add subscripts when several idempotents are used.** **The subscript of an idempotent is numeric when it counts and a role label when it names, but for the two members of a complete sign pair.** A pair is $\tilde\Pi_1, \tilde\Pi_2$; a second pair occurring in the same statement takes the next numbers, $\tilde\Pi_3, \tilde\Pi_4$; and a family indexed by a direction is written with its argument, $\tilde\Pi_\pm(\tilde\Xi)$. When a pair is **complete**, $\tilde\Pi_+ + \tilde\Pi_- = e_0$, its two members may be written $\tilde\Pi_+$ and $\tilde\Pi_-$, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$. A pair that is not complete may be numbered, labelled or signed as the statement requires. A role label is written in upright roman, as for a unit element.

A non-zero idempotent $\tilde\Pi$ generates the **minimal left ideal** $\mathbb{B}\tilde\Pi$; the standard pair, the classification of the idempotents, the polarisation identity, the Peirce decomposition, the matrix units and the projective geometry of the pure states are those of *Idempotents of the General Plain Algebra* and its companions.

The idempotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde\Pi$ | An idempotent or a pure state of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde\Pi$ it generates |
| $\tilde\pi$ | An idempotent of the quaternion or split-quaternion layer |
| $\Pi$ | An idempotent of the complex, split-complex, dual or reduced biquaternion layer, where no tilde is written |

The convention is one of **notation, not of substance**: an element written $\tilde\Pi$ is not a different kind of object from one written $\tilde Q$, only an element known to be idempotent, and the glyph records that knowledge at the point of use; a passage that needs a generic idempotent variable writes $\tilde\Pi$.

### The Nilpotent Convention

The nilpotents carry a symbol of their own, beside the idempotent $\tilde\Pi$ (§*The Idempotent Convention*): the lower-case $\tilde\nu$ of the quaternion and split-quaternion layers and the upper-case $\tilde\Upsilon$ of the biquaternion and split-biquaternion layers, as the case rule requires. **The capital is an upsilon and not a $Y$.**

A **nilpotent** of the algebra is an element $\tilde\nu$ whose square vanishes,

$$
\tilde\nu^2 = 0 .
$$

**The square is read in a named product**, the algebra product unless the statement names another: the corpus writes nilpotents in the four general products of *Zero Divisors in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* as well, and the class is relative to the product — an element square-zero in the plain product need not be square-zero in the general plain sesquilinear one, and in the plain antisymmetric block every central element is square-zero, the unit among them. **No nilpotent is a Hermitian idempotent**, a Hermitian nilpotent being zero, so no nilpotent is a pure state; it is nevertheless the partner of the idempotent in a minimal left ideal — for the standard pair $\mathbb{B}\hat\Upsilon_2 = \mathbb{B}\tilde\Pi_1$ — and its products with its star are Hermitian idempotents of that ideal.

**The coordinates carry the letter of the nilpotent**, as for a general element: in $\mathbb{B}$ the nilpotent is $\tilde\Upsilon = \Upsilon_0e_0 + \Upsilon_1e_1 + \Upsilon_2e_2 + \Upsilon_3e_3$ with $\Upsilon_\mu = \nu_\mu + i\nu'_\mu$, its scalar part $\Upsilon_0$ and its vector part $\vec\Upsilon = \vec\nu + i\vec\nu'$; in $\mathbb{H}$ it is $\tilde\nu = \nu_0e_0 + \nu_1e_1 + \nu_2e_2 + \nu_3e_3$ with real $\nu_\mu$.

**It is allowed to add subscripts when several nilpotents are used.** **The subscript of a nilpotent is numeric when it counts and a role label when it names**, as for the idempotents apart from their complete sign pair: where more than one occurs a pair is $\tilde\nu_1, \tilde\nu_2$, a second pair in the same statement takes the next numbers, and where a nilpotent plays a named role it carries the role in upright roman as its subscript. A sign is a subscript where the statement needs one.

The nilpotents have no classification of the idempotent kind. The square-zero set is not one family, and which set it is depends on the product: the elements of zero norm under the general quaternionic product, the pure isotropic vectors under the associative one. The standard units and the instances are those of *Nilpotents of the General Quaternionic Algebra*, *Idempotents of the General Plain Algebra* and *Ideals and Peirce Decomposition of the Biquaternion Algebra*. The standard pair of nilpotents is the two off-diagonal Peirce units of the last of these, $\hat\Upsilon_1$ and $\hat\Upsilon_2$, exchanged by the star.

The nilpotent glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde\Upsilon$ | A nilpotent of the biquaternion or split-biquaternion layer, and the minimal left ideal $\mathbb{B}\tilde\Upsilon$ it generates |
| $\tilde\nu$ | A nilpotent of the quaternion or split-quaternion layer |
| $\hat\Upsilon$, $\hat\nu$ | A pure nilpotent, written with the hat and without the tilde by the priority rule of §*Pure Elements and their Coefficients* |
| $\Upsilon$ | A nilpotent of the complex, split-complex or dual layer, where no tilde is written |

The convention is one of **notation, not of substance**: an element written $\tilde\nu$ is not a different kind of object from one written $\tilde Q$, only an element known to be nilpotent.

**The standard pair carries the hat, not the tilde.** The two off-diagonal Peirce units are pure, $\hat\Upsilon_1 = \tfrac12(ie_1 - e_2)$ and $\hat\Upsilon_2 = \tfrac12(ie_1 + e_2)$, with no scalar part, so by §*Pure Elements and their Coefficients* the hat takes priority over the tilde and the tilde is dropped; the pair is written $\hat\Upsilon_1, \hat\Upsilon_2$ and never $\tilde\Upsilon_1, \tilde\Upsilon_2$. The tilde is kept for the general nilpotent $\tilde\Upsilon$, which may carry a scalar part and is not pure.

## The Form Convention, the Norm Convention and the Unitary Convention

The corpus writes a **generic form** and a **generic norm**, the norm being the form read at its two equal arguments:

$$
\mathrm{Form}(\tilde P,\tilde Q) , \qquad \mathrm{Norm}(\tilde Q) = \mathrm{Form}(\tilde Q,\tilde Q) .
$$

**One bracket, two arities.** A **bracket** names a **form** when it carries two arguments and its **algebraic norm** when it carries one, the single argument standing for the two equal ones:

$$
\langle\tilde P,\tilde Q\rangle_{ab}=\mathrm{Sc}\bigl(\tilde P^{\,a}\tilde Q^{\,b}\bigr) , \qquad \langle\tilde Q\rangle_{ab}=\langle\tilde Q,\tilde Q\rangle_{ab} ,
$$

the subscript recording the pair of slots. The convention is one of **notation, not of substance**: the pair is the form and the norm of the statement at hand. The two definitions — the form of an operation as its scalar part read in two arguments, bilinear or sesquilinear by its second slot, and the algebraic norm as that form at its two equal arguments — and the four brackets, $\langle\cdot,\cdot\rangle$ the plain, $\langle\cdot,\cdot\rangle_{*}$ the Hermitian, $\langle\cdot,\cdot\rangle_{\natural}$ the quaternionic and $\langle\cdot,\cdot\rangle_{\natural*}$ the Krein, are *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* and *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*.

**The four names stand on the four norms, and the form is the norm read in two slots.** One name runs over the three levels of the product, the form and the norm: the **plain** bracket is the scalar part of the plain bilinear product, the **Hermitian** bracket that of the plain sesquilinear product, the **quaternionic** bracket that of the quaternionic bilinear product, and the **Krein** bracket that of the quaternionic sesquilinear product. Read on one argument the four are the **plain norm**, the **Hermitian norm**, the **quaternionic norm** and the **Krein norm**. The four products, their forms and their norms go together, one to a row:

| Product | Form | Norm |
|---|---|---|
| the general plain bilinear | $\langle\tilde P,\tilde Q\rangle$ | the plain norm $\langle\tilde Q\rangle$ |
| the general plain sesquilinear | $\langle\tilde P,\tilde Q\rangle_{*}$ | the Hermitian norm $\langle\tilde Q\rangle_{*}$ |
| the general quaternionic bilinear | $\langle\tilde P,\tilde Q\rangle_{\natural}$ | the quaternionic norm $\langle\tilde Q\rangle_{\natural}$ |
| the general quaternionic sesquilinear | $\langle\tilde P,\tilde Q\rangle_{\natural*}$ | the Krein norm $\langle\tilde Q\rangle_{\natural*}$ |

### The Unitary Convention

The unit elements carry a glyph of their own, beside the root $\tilde\Xi$ (§*The Root Convention*), the idempotent $\tilde\Pi$ (§*The Idempotent Convention*) and the nilpotent $\tilde\nu$ (§*The Nilpotent Convention*): the **u**, in the two cases.

**A unit element is an element of norm one, and the norm is the one in view.** **The letter $u$ is reserved for unit elements.** Every occurrence of $u$, $\tilde u$, $\hat u$ or $U$ names an element of norm one; a general element is $\tilde q$ or $\tilde Q$, a pure element $\hat q$ or $\hat Q$, and a scalar field, a velocity or a generic vector is never written $u$. **The exponential is written $\exp(\cdot)$**, never $e^{\cdot}$: the letter $e$ is kept for the basis $e_0,e_1,e_2,e_3$ and for the electric charge. The glyph is the generic norm above read at the central value $e_0$,

$$
\mathrm{Norm}(\tilde U) = e_0 ,
$$

so that it names no set until the norm is named. The convention is **relative to the norm**: the norm-one set is the level set of that norm, it depends on the form exactly as the norm does, and a statement that writes $\tilde U$ names its norm — the plain, the Hermitian, the quaternionic or the Krein norm in the biquaternion layer, the plain or the quaternionic norm in the quaternion layer. The same glyph stands for the unit quaternion under one norm and for a point of another level set under another, and the norm is what tells them apart.

**The norm-one set, norm by norm.** In the biquaternion layer the four norms give four level sets, all written against the central values $e_0$ or $1$:

| Norm | the condition $\mathrm{Norm}(\tilde U)=e_0$ | the norm-one elements |
|---|---|---|
| $\langle\tilde Q\rangle$ | $Q_0^2-Q_1^2-Q_2^2-Q_3^2 = e_0$ | the complex hyperboloid of the plain norm |
| $\langle\tilde Q\rangle_{\natural}$ | $Q_0^2+Q_1^2+Q_2^2+Q_3^2 = e_0$ | $\mathbb{B}^{\times}_1$, the norm-one units |
| $\langle\tilde Q\rangle_{*}$ | $\lvert Q_0\rvert^2+\lvert Q_1\rvert^2+\lvert Q_2\rvert^2+\lvert Q_3\rvert^2 = 1$ | the unit sphere of the Hermitian norm |
| $\langle\tilde Q\rangle_{\natural*}$ | $\lvert Q_0\rvert^2-\lvert Q_1\rvert^2-\lvert Q_2\rvert^2-\lvert Q_3\rvert^2 = 1$ | the indefinite level set of the Krein norm |

The two bilinear norms are complex-valued, so their level sets are complex and the condition is read $=e_0$ with $e_0$ the central reality; the two sesquilinear norms are real-valued, so their level sets are real and the condition is read $=1$.

**The quaternion layer, and the rotors.** In the quaternion layer the norm is the quaternion norm, and its level set is the sphere

$$
Sp(1)=\{\tilde u\in\mathbb{H}:\tilde u\tilde u^{\natural}=e_0\}=\{\tilde u\in\mathbb{H}:u_0^2+u_1^2+u_2^2+u_3^2=1\}=S^{3}=\mathrm{SU}(2),
$$

the **unit quaternions**, the double cover of $SO(3)$ by $\tilde u\mapsto\iota_{\tilde u}$. **The rotors are these elements**: the orientation rotor of the rotation articles, of quaternion norm $e_0$, is a unit real quaternion and is therefore written $\tilde u$. The quaternion layer is the case where the two readings of the word agree, because the quaternion norm is multiplicative and its norm-one set is at the same time a group, $Sp(1)$.

**The group condition is narrower than the norm-one condition.** Where the form in view is the sesquilinear one and the element is asked not only to have norm one but to preserve the form, $\tilde U^{*}\tilde U=e_0$, the norm-one elements that do so form the **unitary group**,

$$
U(\mathbb{B})=\{\tilde U:\tilde U^{*}\tilde U=e_0\}\cong U(2).
$$

Every such element has $\langle\tilde U\rangle_{*}=e_0$, so the group sits inside the norm-one set of the Hermitian norm; the group is written with the group letter, $U(\mathbb{B})$ or $U(2)$, and never with the tilde of an element. The name **unitary** is the name of that group, and the glyph $\tilde U$ is the norm-one element, which is the wider notion.

**The layers and their involutions.** The norm and the group condition have a sense only where the involution they use exists: the bar alone over $\mathbb{C}$ and the split-complex numbers, the natural sign alone over $\mathbb{H}$ and the split-quaternions, and all four marks over $\mathbb{B}$ and the split-biquaternions. A layer with no star has no Hermitian and no Krein form, so its unit elements are those of a bilinear form alone.

**The case rule splits the glyph, as it does for the elements, the idempotents, the nilpotents and the roots.** The unit elements of the biquaternion and split-biquaternion layers carry the upper-case tilde, $\tilde U$; those of the quaternion and split-quaternion layers carry the lower-case tilde, $\tilde u$; and those of the complex, split-complex, dual and reduced biquaternion layers carry the plain capital, $U$, no tilde being written where there is no quaternionic factor.

**The coordinates carry the letter of the unit element**, as for a general element: in $\mathbb{B}$ it is $\tilde U = U_0e_0 + U_1e_1 + U_2e_2 + U_3e_3$ with $U_\mu = u_\mu + iu'_\mu$, its scalar part $U_0$ and its vector part $\vec U = \vec q_a + i\vec q'_a$; in $\mathbb{H}$ it is $\tilde u = u_0e_0 + u_1e_1 + u_2e_2 + u_3e_3$ with real $u_\mu$.

**It is allowed to add subscripts when several unit elements are used.** **The subscript of a unit element is numeric when it counts and a role label when it names.** Where more than one occurs the elements are numbered, $\tilde U_1, \tilde U_2$; where the unit elements of a statement play named roles, each carries the role in upright roman as its subscript, for instance $\tilde U_{\mathrm b}$ for a boost factor and $\tilde U_{\mathrm r}$ for a rotation factor. A sign is a subscript where the statement needs one, as in $\tilde U_+$ and $\tilde U_-$.

The glyph is therefore **split by the case rule**, and the split is the reason the convention is stated:

| Symbol | Role |
|---|---|
| $\tilde U$ | A unit element of the biquaternion or split-biquaternion layer, $\mathrm{Norm}(\tilde U)=e_0$ |
| $\hat U$ | A unit pure biquaternion, the pure case of $\tilde U$, of norm one |
| $\tilde u$ | A unit element of the quaternion or split-quaternion layer, a unit quaternion, $Sp(1)$ |
| $\hat u$ | A unit pure quaternion, the pure case of $\tilde u$; the axis of a rotation |
| $U$ | A unit element of the complex, split-complex, dual or reduced biquaternion layer |

**The pure case of the unit element carries the hat, and the two pure unit glyphs are $\hat u$ and $\hat U$.** The pure form of the unit element is written with the hat of its layer and without the tilde: $\hat u$ in the quaternion and split-quaternion layers, $\hat U$ in the biquaternion and split-biquaternion ones, read off the general unit element by $\tilde u \to \hat u$ and $\tilde U \to \hat U$.

The convention is one of **notation, not of substance**: an element written $\tilde U$ is not a different kind of object from one written $\tilde P$, only an element known to have norm one. It is **relative to the norm**, and it says nothing until the norm is named — the same glyph is the unit quaternion under the quaternionic norm in the quaternion layer and a point of another level set under the Hermitian norm in the biquaternion layer. The letter is not free for a generic element: an arbitrary element is $\tilde P$ or $\tilde Q$, a root is $\tilde\Xi$, an idempotent $\tilde\Pi$, a nilpotent $\tilde\nu$ or $\tilde\Upsilon$.

### The Letters $U$ and $u$ Outside the Layers

The reservation above is **local to the layers of the biquaternion family** — the complex, split-complex, dual and reduced biquaternion layers, the quaternion, split-quaternion, biquaternion and split-biquaternion layers, and the operator articles built on them. Inside them the glyphs $u$, $\tilde u$, $\hat u$, $U$, $\tilde U$ and $\hat U$ name unit elements and nothing else, and a velocity, a scalar field or a generic vector is never written with either letter. Outside them the two letters are **borrowed**, and each borrowing is fixed rather than left open:

| Borrowed meaning | Glyph | What keeps it apart |
|---|---|---|
| the unitary group of a form | $U(n)$, $U(H)$, $U(A)$, $U(\mathbb B)$ | the argument is a number, a Hilbert space or an algebra, never a unit element |
| the universal enveloping algebra | $U(\mathrm G)$ | the argument is a Lie algebra — the upright roman $\mathrm G$ in the enveloping articles, the fraktur $\mathfrak g$ where the article's Lie algebra is fraktur — and the unitary group never takes a Lie algebra |
| the group of units of a ring | $R^{\times}$ | the corpus writes the group of units with the cross, never as $U(R)$ |
| an open set or a neighbourhood; a space and its quotient | $U$; $V$, $V/U$ | local to the topological and functional-analysis articles, which carry no unit element |
| a family of sets, or a named quantity kept off the element $U$: an open cover, a filter or ultrafilter, a uniformity; the set of unit elements of a layer | $\mathcal U$ | the calligraphic script separates it from the upright $U$, and the meaning is the article's own |
| an internal energy | $U$ | local to the thermodynamics articles, where it is a functional of the state |
| a velocity, a speed, a four-velocity | $v$ for a velocity and $V$ for a four-velocity: $\vec v$, $v_i$, $v=\lvert\vec v\rvert$, the four-velocity $\tilde V$, the unit four-velocity $\tilde v=\tilde V/c$ | **neither $u$ nor $U$ is ever a velocity**, in any article |
| an up quark, an atomic mass unit | the upright roman $\mathrm u$ | the upright roman is a particle or a unit, the italic is an element |
| an unknown function or a wave field | $u(x,t)$ | local to the analysis and partial-differential-equation articles |
| a uniform law | $\mathrm{Unif}(a,b)$ | the corpus names the law and never writes a bare $U$ for it |

**Two of the rows are rules of the corpus itself and not borrowings.** A **velocity** is written $v$ and distinguished by a subscript — $v_i$ for a component, $v_x$ for the component along an axis, $v=\lvert\vec v\rvert$ for a speed, $v^{\mu}$ for the components of a four-velocity, the four-velocity itself being the element $\tilde V$ and a four-velocity reduced to unit norm being $\tilde v=\tilde V/c$ — and neither letter of the unit element, $u$ or $U$, is allowed against any velocity. **It is allowed to add subscripts when several velocities are used**, as for the other kinds of element: $\tilde V_1,\tilde V_2$ for two four-velocities, $\tilde v_a$ for a unit four-velocity, $\vec v_b$ for a boost velocity. An **up quark** and an **atomic mass unit** are written in the upright roman, $\mathrm u$, against the italic $u$ of an element. The other rows are borrowings the corpus accepts and keeps out of the algebra layer by an argument or by the article; a borrowing never displaces the reservation inside the layers.

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

**The word "interval".** Two different objects share the word, and the corpus keeps them apart. In the mathematical corpus an **interval** is an order-theoretic or lattice object: a convex subset of a linearly ordered set, the interval $[a,b]=\{x:a\le x\le b\}$ of a lattice or of a poset of effects, defined by the order and not by a form. In the physical corpus the **interval** is the value of the quadratic form, $\langle\tilde Q\rangle_{\natural}=(ic\,t)^2+\vec x^2=\vec x^2-c^2t^2$ on the material sector, defined by the form and not by an order. A statement about the sign of the interval is therefore never a statement about a lattice interval, and a lattice interval is never the line element; where the two senses could meet, the corpus writes *the form value* or *the quadratic form* for the physical one.

## The Superscripts

Two superscript tokens run beside the marks of the elements and the marks of the conjugations, and neither is to be read for the other:

| Token | Written on | Meaning |
|---|---|---|
| $^{\mathrm{fop}}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $^{\mathrm{opp}}$ | an algebra name | the opposite algebra, the algebra with the reversed product |

The marks of the elements — the case, the prime, the tilde, the arrow and the hat — say what a glyph **is**, not that a glyph is an **operator**, and no mark is needed to say it. On this algebra **an operator is a multiplication by an element**: every element acts on the algebra, so an operator whose letter is the letter of an element **is** that element and keeps the element's glyph. The left and right multiplications $L_a$ and $R_a$, the sandwich $\Theta_{\tilde Q}$, a derivation, an automorphism or a module endomorphism is named by a glyph of its own and read as an operator from that glyph, not from a mark.

**The mark, and its one use.** The single exception is the **Fock layer** of the physical corpus, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the upright superscript $\mathrm{fop}$, set on the glyph:

$$
a^{\mathrm{fop}},\quad b^{\mathrm{fop}},\quad a^{\mathrm{fop}\dagger},\quad \psi^{\mathrm{fop}},\quad N^{\mathrm{fop}},\quad H^{\mathrm{fop}},\quad F^{\mathrm{fop}},\quad Q^{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $p$, the position $x$, the spin $S$ and the parity, charge-conjugation and time-reversal maps $P$, $C$ and $T$ carry no superscript, because each is an element acting by multiplication or a map with a glyph of its own.

**It combines with the dagger, the mark first.** The dagger is the general adjoint (§*The Conjugations and the Adjoint*). Where both marks fall on one glyph the Fock mark comes first and the adjoint follows, $(a^{\mathrm{fop}})^{\dagger}$, contracted to $a^{\mathrm{fop}\dagger}$; the dagger alone never marks a glyph as an operator, and the superscript alone never asserts self-adjointness.

**The opposite algebra carries a different token.** The **opposite algebra**, whose multiplication is reversed, $a\cdot b=ba$, carries the superscript $\mathrm{opp}$ — $A^{\mathrm{opp}}$, $\mathbb{B}^{\mathrm{opp}}$, $M_n(D)^{\mathrm{opp}}$ — and it is the **algebra name** that takes the mark; the Fock token $\mathrm{fop}$ marks a Fock-operator glyph. The two meanings are separated by the token itself and not by context.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_0$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}_{\mathrm{r}}$, because a bare underscore would take the first character alone.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the general elements, the units, the roots, the idempotents and the nilpotents alike: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $Q_0, Q_1, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}_{\mathrm{r}}$ and $\tilde U_{\mathrm r}$.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $Q_0$, $Q_1$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{\mu\nu}$ |
| a sign | $Q_\pm$ |
| an upright word | $\mathbb{B}_{\mathrm{r}}$, $\tilde U_{\mathrm r}$ |
| a grouped expression | $Q_{n+1}$ |

## Summary

The conventions are of two kinds: the mathematical notation, and the working conventions of the corpus.

A generic element of a number system is written as a linear combination of the basis with its coefficients in
the scalar sector of the system, the biquaternion element being $\tilde Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$
with $Q_\mu = q_\mu + iq'_\mu$. The generic element of a system carries a letter of its own: $\alpha, \beta$ for the Booleans, $n, m$ for the naturals and the integers, $a, b, c$ for the rationals and the reals, $A = a + ia'$, $B = b + ib'$ for the commutative two-parameter systems, and $T = A + Bj$ for the reduced biquaternions, whose two coordinates are complex and whose second unit is the hyperbolic $j$, and $o = o_0e_0 + \cdots + o_7e_7$ for the octonions. The notation is fixed here above all for the conjugations, which is where the corpus has the most marks to keep apart, and for the number systems, whose glyphs carry two bits each. An algebra with a degree-2 form carries an intrinsic conjugate, the map that negates its vectors and fixes its scalars; it is written with a **natural sign**. The involution of the base extends to the coefficients and is written with a **bar**. Their composite is the Hermitian anti-automorphism, written with a **star**; its negative is the **anti-Hermitian** conjugation, written **flat**; and the **dagger** is the adjoint of an operator, written on operators and never on the elements. The star and the bar commute, $^{*} = \bar{\cdot}\circ{}^{\natural} = {}^{\natural}\circ\bar{\cdot}$, the flat is $\flat = -{}^{*}$, and $\{\mathrm{id}, \bar{\cdot}, {}^{\natural}, {}^{*}\}$ is a Klein four-group while the flat stands outside it. The corpus writes a **form** with two arguments and its **algebraic norm** with one, the generic pair $\mathrm{Form}(\tilde P,\tilde Q)$ and $\mathrm{Norm}(\tilde Q)=\mathrm{Form}(\tilde Q,\tilde Q)$. On a base whose involution is the identity the bar is the identity map and the star coincides with the natural sign.

On the number systems the **case** records whether the commuting scalar sector is larger than the reals and the **tilde** records the presence of the quaternionic factor, and the two are read independently: $a$ is real, $A$ complex or split-complex or dual, $T$ reduced biquaternion — upper case and no tilde, with two complex coordinates — $\tilde q$ quaternion or split-quaternion, $\tilde Q$ biquaternion or split-biquaternion, and $o$ octonion — no tilde, the octonions having no quaternionic factor. A **pure element** — one with no scalar part — drops the tilde and carries the hat, $\hat q$ in the quaternion and split-quaternion layers and $\hat Q$ in the biquaternion and split-biquaternion ones. The **idempotents**, the **nilpotents** and the **roots** carry symbols of their own, split by the same case rule: $\tilde\Pi$ is an idempotent or a pure state of the biquaternion and split-biquaternion layers, and the minimal left ideal it generates, $\tilde\pi$ the same in the quaternion and split-quaternion layers, and $\Pi$ in the complex, split-complex and dual layers where no tilde is written; $\tilde\nu$ is a nilpotent of the quaternion or split-quaternion layer and $\tilde\Upsilon$ a nilpotent of the biquaternion or split-biquaternion layer; $\tilde\Xi$ is a root of $1$ of the biquaternion and split-biquaternion layers and $\tilde\xi$ the same in the quaternion and split-quaternion layers; while $\tilde P$ is the generic element of a statement that holds for every element. The upper-case tilde carries four roles — the idempotent, the nilpotent, the root and the generic element — and the split is deliberate.

The working conventions are the corpus's own. Every article is registered in exactly one menu, with a comment that outlines it, and a leading `+` marks a planned article. The four groups of a category — Theory, Operator Theory, `*` Theory and `*` Operator Theory — each add one thing to the group before, the star naming the involutive layer on the elements and then on the operators, so that the last group holds the operators built from the involution, and the group `Applications` closes the category. A concept is introduced once, in the category that owns it, and is cited afterwards rather than restated; every deferral to a later part is stated explicitly, which is how the ordering rule of *Introduction to Mathematics* is enforced. Each article opens with its title and an Introduction and closes with Summary, Summary of Notation and Further Reading.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bar{\cdot}$ | Complex conjugation: the involution of the base, extended to the element |
| ${}^{\natural}$ | Quaternion conjugation: the intrinsic conjugate of the algebra |
| ${}^{*}$ | Hermitian conjugation, the composite of the bar and the natural sign |
| ${}^{\flat} = -{}^{*}$ | Anti-Hermitian conjugation |
| ${}^{\dagger}$ | The general adjoint of an operator, of which the star is the instance in the positive definite form; written on operators and never on elements |
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}_{\mathrm{r}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}, \mathbb{O}$ | The number systems of the corpus, in the order the corpus reaches them |
| Lower case, upper case | The scalar sector is the reals, or larger than the reals |
| Tilde | The presence of the quaternionic factor |
| Arrow | The vector part of a named element — $\vec q$, $\vec Q$ or $\vec o$ |
| Hat | A pure element, an element with no scalar part — $\hat q$ and $\hat Q$ (§*Pure Elements and their Coefficients*) |
| $\alpha, \beta$; $n, m$; $a, b, c$ | The generic elements of the Booleans, the naturals and the integers, and the rationals and the reals |
| $A = a + ia'$, $B = b + ib'$ | The generic element of a commutative two-parameter system, with $j$ or $\varepsilon$ in place of $i$, and the imaginary coefficient carrying a prime |
| $T = A + Bj$ | The generic element of the reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, upper case with no tilde, its two coordinates $A = a + ia'$ and $B = b + ib'$ complex and its second unit the hyperbolic $j$, $j^{2} = +1$ and $ji = ij$, on the basis $1, i, j, ij$ |
| $o = o_0e_0 + \cdots + o_7e_7$ | The generic element of the octonion algebra $\mathbb{O}$, lower case with no tilde; the coordinates are $o_\mu$ and the vector part $\vec o$ |
| $\tilde\Xi$ | A root of $1$ of the biquaternion or split-biquaternion layer |
| $\tilde\xi$ | A root of $1$ of the quaternion or split-quaternion layer |
| $\Xi$ | A root of $1$ of the complex, split-complex or dual layer |
| $\tilde\Pi$ | An idempotent or a pure state of the biquaternion or split-biquaternion layer, and the minimal left ideal it generates |
| $\tilde\pi$ | An idempotent of the quaternion or split-quaternion layer |
| $\Pi$ | An idempotent of the complex, split-complex, dual or reduced biquaternion layer |
| $\tilde\nu$ | A nilpotent of the quaternion or split-quaternion layer |
| $\tilde\Upsilon$ | A nilpotent of the biquaternion or split-biquaternion layer |
| $\tilde U$ | A unit element of the biquaternion or split-biquaternion layer, $\mathrm{Norm}(\tilde U)=e_0$; the norm is the one in view (§*The Unitary Convention*) |
| $\hat U$ | A unit pure biquaternion, the pure case of $\tilde U$, of norm one |
| $\tilde u$ | A unit element of the quaternion or split-quaternion layer, a unit quaternion, $Sp(1)$ |
| $\hat u$ | A unit pure quaternion, the pure case of $\tilde u$; the axis of a rotation |
| $U$ | A unit element of the complex, split-complex, dual or reduced biquaternion layer |
| $\hat q$ | A pure element of the quaternion or split-quaternion layer, an element with no scalar part |
| $\hat Q$ | A pure element of the biquaternion or split-biquaternion layer |
| $^{\mathrm{fop}}$ | A **Fock operator**, an operator on the Fock space and not an element of the algebra — $a^{\mathrm{fop}}$, $N^{\mathrm{fop}}$, $H^{\mathrm{fop}}$ (§*The Superscripts*). No other operator carries the mark. The opposite algebra uses the separate token $A^{\mathrm{opp}}$ |
| $\tilde P$ | The generic element of the algebra, in a statement that holds for every element |
| $\mathrm{Form}(\tilde P,\tilde Q)$, $\mathrm{Norm}(\tilde Q)=\mathrm{Form}(\tilde Q,\tilde Q)$ | The generic form and the generic norm (§*The Form Convention, the Norm Convention and the Unitary Convention*) |
| $\langle\tilde P,\tilde Q\rangle$, $\langle\tilde Q\rangle$ | The generic bracket, the form in two arguments and the norm in one; the subscript records the pair of slots — plain, $*$ Hermitian, $\natural$ quaternionic, $\natural*$ Krein (§*The Form Convention, the Norm Convention and the Unitary Convention*) |
| `- Theory`, `- Operator Theory`, `- * Theory`, `- * Operator Theory` | The four groups of a category, in that order |
| `- Applications` | The group that closes a category with the concrete instances of its structure |
| `+` | A planned article, registered in the menu and not yet written |
| `articles_maths/<slug>.md` | The file of a mathematical article; the slug is the title in lower case with hyphens |
| Introduction, thematic sections, Summary, Summary of Notation, Further Reading | The skeleton of every article |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853). The original formulation, and the source of the quaternion conjugation and its notation.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
- James Cockle, "On a new imaginary in algebra", *Philosophical Magazine* **34** (1849) 37–47. The tessarines, the commutative algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ that the corpus records as the reduced biquaternions, and the earliest occurrence of the hyperbolic versor.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022. The reduced biquaternion algebra of the engineering literature, its idempotent decomposition, its ring-valued norm and its transform.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution, the first and the second kind, and the classification of their involutions.
- Nicolas Bourbaki, *Éléments de mathématique* (Hermann, then Springer). The model for a notation fixed once and used without variation.
- Donald E. Knuth, *The TeXbook* (Addison-Wesley, 1984). The typographic conventions the source of the corpus follows.
