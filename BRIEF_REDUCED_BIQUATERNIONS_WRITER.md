# __Brief — Writing the Reduced Biquaternions Category__

One self-contained brief, meant to be pasted as the first message of a writing conversation. The work is
53 articles, delivered in **six batches of 10, 10, 10, 10, 10 and 3**; each batch is handed over and
accepted before the next one starts. Nothing is launched by this file.

This brief **supersedes** `BRIEFS_REDUCED_BIQUATERNIONS.md`, which planned 145 articles across eleven
agents, including a `Reduced Biquaternioid Algebraic Structures` category that the author has since
**rejected**. The current menu is `## Reduced Biquaternions` in `maths.md`, 53 planned articles, and this
brief is cut to fit it.

---

## 0. The object, the conventions and the rules

**The object.** The reduced biquaternion space is the commutative algebra

$$\mathbb{B}_{\mathrm{r}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C},$$

with the basis $1, i, j, ij$, the relations $i^{2} = -1$, $j^{2} = +1$, $ji = ij$, and the two idempotents
$\Pi_{1,2} = \tfrac12(1\pm j)$. An element is $T = A + Bj$ with $A = a + ia'$ and $B = b + ib'$ complex, and
the idempotent decomposition is $T = (A+B)\Pi_1 + (A-B)\Pi_2$. It is the engineering **reduced
biquaternion** algebra, equivalently the **tessarines**, the **double-complex** numbers or the
**commutative hypercomplex** algebra. The glyph $\mathbb{B}_{\mathrm{r}}$ and the element $T = A+Bj$ are
fixed in *Conventions in Mathematics*, §*The Elements and their Coefficients*.

**The involutions.** The **bar** conjugates the coefficients, $\overline{A+Bj} = \bar A + \bar B j$; the
**natural sign** ${}^{\natural}$ negates the second slot, $(A+Bj)^{\natural} = A - Bj$; the **star** is
their composite, ${}^{*} = \bar{\cdot}\circ{}^{\natural}$; the **flat** is ${}^{\flat} = -{}^{*}$.

**The four general products.** On $T = A+Bj$ and $W = C+Dj$:

| product | value | scalar part | $j$-part |
|---|---|---|---|
| the general plain bilinear | $TW$ | $AC+BD$ | $AD+BC$ |
| the general quaternionic bilinear | $T^{\natural}W$ | $AC-BD$ | $AD-BC$ |
| the general plain sesquilinear | $TW^{*}$ | $A\bar C - B\bar D$ | $B\bar C - A\bar D$ |
| the general quaternionic sesquilinear | $T^{\natural}W^{*}$ | $A\bar C + B\bar D$ | $-(A\bar D + B\bar C)$ |

The space is **commutative**, so symmetrisation and antisymmetrisation add nothing to the plain bilinear
product and the general plain sesquilinear product; there are **four** general products, and the twelve
slots carry four scalar parts. Do **not** name the four by acronym, and do **not** discuss collapsed or
dead slots: the author rejects both. Write "the four general products", "the multiplication", "the
general plain bilinear product", and so on. (The clean Biquaternions articles contain no acronym either;
follow them.)

**Three hard warnings.** First, the algebra is commutative and has zero divisors, so there is **no**
division: an element is invertible exactly when both idempotent coordinates are nonzero. Second, the
algebraic norm (an element of the algebra) is **not** the topological norm (a positive real); never
conflate them. Third, the algebra is not a field and not a division algebra; every claim must respect
that.

**The rules (from `PLAN.md`, not negotiable).**

1. Read `/home/hp/.openhands/memory/MEMORY.md` and `PLAN.md` first.
2. Read *Conventions in Mathematics* and *Conventions in the Biquaternion Universe* before writing.
3. Every article: title line `# __Title__`, then `## Introduction`, thematic `##` sections, closing with
   `## Summary`, `## Summary of Notation`, `## Further Reading`.
4. Write the `.md`. When the article is written, **drop the leading `+`**
   from its entry in `maths.md` (the `+` marks a planned article).
5. Cite, do not restate: a concept is introduced once, in the article that owns it. State every deferral.
6. **Verify by recomputation on at most 100 elements** before asserting anything. Scripts are written
   **outside** the repository and deleted afterwards, whatever their location.
7. **Never touch version control or the build** (no `git`, no `build.py`).
8. **Do not launch sub-agents.**
9. Tables are Markdown, never LaTeX arrays. Indent display math four spaces inside a list. Never let `$…$`
   span a line break. Give every thematic intersection a real `###` heading, and define before tabulating.
10. Chat in the plain-words style; chat-math in `$…$` / `$$…$$`.

**The reading list** (the corpus's own articles): *Conventions in Mathematics*; *Conventions in the
Biquaternion Universe*; the clean *Biquaternions* category, article for article, as the template — in
particular *Introduction to the Biquaternion Algebra*, *The Four Products, Their Forms and Their Algebraic
Norms*, *Norm and Invertibility in the Biquaternion Algebra*, *Ideals and Peirce Decomposition of the
Biquaternion Algebra* and the Fractal Geometry articles; the *Split-Complex Numbers* category, which is
the same algebra over $\mathbb{R}$ and the closest sibling; *The Mathematical Study of Biquaternions*.

## 1. The template (copy the clean Biquaternions articles)

A live example is `articles_maths/the-four-products-their-forms-and-their-algebraic-norms.md`; its section
skeleton is

```
# __The Four Products, Their Forms and Their Algebraic Norms__
## Introduction
## <thematic section>
### <subsection>
## Summary
## Summary of Notation
## Further Reading
```

The article carries its decisions and reasons, its verified facts with the sample size, its ownership
and boundary rules and its standing weaknesses in its own sections.

## 2. The work — 53 articles, six batches


### Batch 1 — articles 1–10

#### Introduction to the Reduced Biquaternion Algebra

1. **Reduced Biquaternion Space**
   - slug: `reduced-biquaternion-space`
   - content: the algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C}\oplus\mathbb{C}$, the basis $1, i, j, ij$, the defining relations and the two idempotents $\tfrac12(1\pm j)$.

2. **Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$**
   - slug: `reduced-biquaternions-as-a-vector-space-over-r-and-c`
   - content: the space as a real and as a complex vector space, the change of scalars and the realification.

3. **The Two Involutions and the Group of Involutions**
   - slug: `the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions`
   - content: the tessarine conjugation and the coefficient conjugation, their fixed spaces and the group they generate.

4. **The Four Products, Their Forms and Their Algebraic Norms**
   - slug: `the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions`
   - content: the four general products on the coordinates, the forms they carry and the algebraic norms they define; the relations and the comparison between them.

##### Basic Properties

5. **Introduction to the General Plain Algebra of the Reduced Biquaternions**
   - slug: `introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the definition, the data and the plan.

6. **Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions**
   - slug: `norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the algebraic norm, the invertibility criterion and the group of units.

7. **Zero Divisors of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the zero divisors, the null cone and its structure.

8. **Annihilators of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `annihilators-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the annihilators of an element and the two-sided annihilator of the structure.

9. **Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the roots of $1$, the idempotents and the projections they carry.

10. **Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the roots of $0$ and the nilpotents, product by product.


### Batch 2 — articles 11–20

##### Basic Properties

11. **Square Roots of a General Element in the General Plain Algebra of the Reduced Biquaternions**
   - slug: `square-roots-of-a-general-element-in-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the roots of a general element, with the existence and the count.

##### Advanced Properties

12. **The Specificities of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `the-specificities-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: what the structure adds to the shared theory and what it shares with the others.

13. **Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the two minimal ideals and the Peirce decomposition along the two idempotents.

14. **The Group of Units of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the group of units and the complement of the zero-divisor cone.

15. **The Forms of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `the-forms-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the bilinear and sesquilinear forms the structure carries.

##### Operators

16. **The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions**
   - slug: `the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions`
   - content: the left and right multiplications and the bi-module structure.

##### Representations

17. **The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions**
   - slug: `the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions`
   - content: the structure read in the $2\times2$ matrix element representation.

#### Remarkable Subspaces

18. **Introduction to the Remarkable Subspaces**
   - slug: `introduction-to-the-remarkable-subspaces-of-the-reduced-biquaternions`
   - content: the centre, the vector subspace, the Hermitian and the anti-Hermitian subspaces and the idempotent lines.

19. **Decompositions Along the Remarkable Subspaces**
   - slug: `decompositions-along-the-remarkable-subspaces-of-the-reduced-biquaternions`
   - content: the block decomposition along the two involutions and the decomposition along the idempotents.

20. **Comparison of the Remarkable Subspaces**
   - slug: `comparison-of-the-remarkable-subspaces-of-the-reduced-biquaternions`
   - content: the subspaces at a glance, with defining conditions, bases, dimensions and closure.


### Batch 3 — articles 21–30

#### Reduced Biquaternions Standard Element Representations

21. **Introduction to Reduced Biquaternion Element Representations**
   - slug: `introduction-to-reduced-biquaternion-element-representations`
   - content: the representations of an element and how they are read.

22. **The Four-Vector Element Representation of the Reduced Biquaternions**
   - slug: `the-four-vector-element-representation-of-the-reduced-biquaternions`
   - content: the element as a quadruple of real numbers and as a pair of complex numbers.

23. **Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions**
   - slug: `introduction-to-the-2x2-matrix-element-representation-of-reduced-biquaternions`
   - content: the regular representation and the $2\times2$ matrix model with real or complex entries.

24. **Reduced Biquaternion Other Algebraic Element Representations**
   - slug: `reduced-biquaternion-other-algebraic-element-representations`
   - content: the remaining representations and their comparison.

#### Reduced Biquaternions Polar Element Representation

25. **Reduced Biquaternions Polar Element Representation**
   - slug: `reduced-biquaternions-polar-element-representation`
   - content: the polar form, its uniqueness under the phase-range convention and the two-factor reading.

#### Operators

26. **Operators on the Reduced Biquaternions**
   - slug: `operators-on-the-reduced-biquaternions`
   - content: the operators of the four general products collected and compared.

#### Introduction to Topology on the Reduced Biquaternions

27. **Topology in the Space of Reduced Biquaternions**
   - slug: `topology-in-the-space-of-reduced-biquaternions`
   - content: the topology of the space and its relation to the four general products.

#### Topology of the Reduced Biquaternion Algebra

28. **The Euclidean Topology of the Reduced Biquaternion Algebra**
   - slug: `the-euclidean-topology-of-the-reduced-biquaternion-algebra`
   - content: the Euclidean topology, the unit group as a topological group and the topology of the zero-divisor cone.

#### Metrics of the Reduced Biquaternion Algebra

29. **Topology and Metric for Each of the Operations**
   - slug: `topology-and-metric-for-each-of-the-operations-of-the-reduced-biquaternions`
   - content: the topology and the metric attached to each of the four general products.

### Analysis

30. **Reduced Biquaternion Analysis**
   - slug: `reduced-biquaternion-analysis`
   - content: the analysis on the space and the part the two idempotent factors play.


### Batch 4 — articles 31–40

### Analysis

31. **Reduced Biquaternion Regular Functions**
   - slug: `reduced-biquaternion-regular-functions`
   - content: regular functions and the Cauchy-Riemann system of the algebra.

32. **Reduced Biquaternion Spectral Theory**
   - slug: `reduced-biquaternion-spectral-theory`
   - content: spectral theory for the operators on the algebra.

33. **Reduced Biquaternion Integration**
   - slug: `reduced-biquaternion-integration`
   - content: integration and the integral theorems.

34. **Reduced Biquaternion Elementary Functions**
   - slug: `reduced-biquaternion-elementary-functions`
   - content: the elementary functions and their reduction to two complex factors.

35. **Reduced Biquaternion Higher Special Functions**
   - slug: `reduced-biquaternion-higher-special-functions`
   - content: the higher special functions over the algebra.

36. **Reduced Biquaternion Lie Group and Exponential Structure**
   - slug: `reduced-biquaternion-lie-group-and-exponential-structure`
   - content: the exponential and the Lie group structure of the unit group.

37. **Reduced Biquaternion Discrete Harmonic Analysis**
   - slug: `reduced-biquaternion-discrete-harmonic-analysis`
   - content: the discrete reduced biquaternion Fourier transform and the idempotent reduction.

38. **Reduced Biquaternion Continuous Harmonic Analysis**
   - slug: `reduced-biquaternion-continuous-harmonic-analysis`
   - content: the continuous transform, the convolution theorem and the Bochner theorem.

39. **Fueter Theory for Reduced Biquaternions**
   - slug: `fueter-theory-for-reduced-biquaternions`
   - content: the Fueter theory on the algebra.

### Geometry

40. **Reduced Biquaternion Rotations and Lorentz Transformations**
   - slug: `reduced-biquaternion-rotations-and-lorentz-transformations`
   - content: the elliptic and the hyperbolic rotation the two factors carry.


### Batch 5 — articles 41–50

### Geometry

41. **Reduced Biquaternion Automorphisms and Derivations**
   - slug: `reduced-biquaternion-automorphisms-and-derivations`
   - content: the automorphisms and the derivations of the algebra.

42. **The Null Quadric and its Projective Geometry**
   - slug: `the-null-quadric-and-its-projective-geometry-for-the-reduced-biquaternions`
   - content: the null quadric of the norm and its projective geometry.

43. **Reduced Biquaternion Versors and the Orthogonal Group**
   - slug: `reduced-biquaternion-versors-and-the-orthogonal-group`
   - content: the versors and the orthogonal group of the bilinear form.

44. **The Unitary Group of the Reduced Biquaternion Algebra**
   - slug: `the-unitary-group-of-the-reduced-biquaternion-algebra`
   - content: the unitary group of the Hermitian form and its decomposition.

45. **Reduced Biquaternions and Hyperbolic Geometry**
   - slug: `reduced-biquaternions-and-hyperbolic-geometry`
   - content: the hyperbolic geometry the indefinite form carries.

46. **Reduced Biquaternion Objects and their Matrix Correspondences**
   - slug: `reduced-biquaternion-objects-and-their-matrix-correspondences`
   - content: the objects of the geometry and their matrix correspondences.

47. **Reduced Biquaternion Spin Geometry**
   - slug: `reduced-biquaternion-spin-geometry`
   - content: the spin geometry of the algebra.

#### Fractal Geometry

48. **The Reduced Biquaternion Quadratic Map and its Julia Sets**
   - slug: `the-reduced-biquaternion-quadratic-map-and-its-julia-sets`
   - content: the quadratic family and its Julia sets.

49. **The Idempotent Decomposition and the Split Fractal**
   - slug: `the-idempotent-decomposition-and-the-reduced-biquaternion-split-fractal`
   - content: the reduction of the dynamics to the two complex factors.

50. **The Slices of the Reduced Biquaternion Julia Sets**
   - slug: `the-slices-of-the-reduced-biquaternion-julia-sets`
   - content: the slices of the Julia sets and their comparison.


### Batch 6 — articles 51–53

#### Fractal Geometry

51. **The Reduced Biquaternion Iterated Function Systems**
   - slug: `the-reduced-biquaternion-iterated-function-systems`
   - content: the contractions and the self-similar sets they produce.

52. **The Reduced Biquaternion Mandelbrot Set and the Connectedness Locus**
   - slug: `the-reduced-biquaternion-mandelbrot-set-and-the-connectedness-locus`
   - content: the connectedness locus and the effect of the zero divisors.

53. **The Hausdorff Dimension of the Reduced Biquaternion Julia Sets**
   - slug: `the-hausdorff-dimension-of-the-reduced-biquaternion-julia-sets`
   - content: the Hausdorff dimension of the Julia sets.

## 3. How to run one batch

1. Read §0 and §1, *Conventions in Mathematics*, *Conventions in the Biquaternion Universe*, and the two
   or three counterpart Biquaternion articles named in each entry.
2. Write the articles of the batch in order. For each: write `articles_maths/<slug>.md`, then drop the leading `+` from that slug's entry in `maths.md`.
3. Verify every quantitative claim by recomputation on at most 100 elements, with the script outside the
   repository, and report the verification.
4. When the batch is done, report: the slugs written, the `+` dropped, the verifications run, and any
   contradiction found in a neighbour article, with the patch you applied.

## 4. Acceptance

A batch is accepted when every article of the batch exists as `.md`, follows the template,
carries its `+` dropped in `maths.md`, names the reduced biquaternion object and its involutions exactly
as in §0, names the four products without acronym and without the dead-slot discussion, and states the
commutativity, the zero divisors and the absence of division wherever they bear on the result. The menu
must show that slug as a resolved link: the `+` gone, and no broken link introduced.

## 5. Pending decisions — do not act, ask the author

- The twelve `General Plain Algebra of the Reduced Biquaternions` slugs (articles 5 to 17) follow
  `BRIEFS_REDUCED_BIQUATERNIONS.md`. The author may want them renamed to the `Reduced Biquaternion
  Algebra` (the GPA purge done in the clean categories). Write the slugs as they stand, and ask.
- Article 15, *The Forms of the General Plain Algebra of the Reduced Biquaternions*, overlaps article 4,
  which already owns the forms and the algebraic norms. The author may replace it with a *Modules over the
  Reduced Biquaternion Algebra* article, as in the clean Biquaternions. Wait for the word.
