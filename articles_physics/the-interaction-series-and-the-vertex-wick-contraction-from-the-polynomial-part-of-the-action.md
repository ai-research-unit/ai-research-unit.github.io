# __The Interaction Series and the Vertex: Wick Contraction from the Polynomial Part of the Action__

## Introduction

**The claim.** Stage $3$ turns the interaction into a series of local objects. Expanding the exponential of $S_{\mathrm{int}}$, each factor of $S_{\mathrm{int}}$ is an integral of a polynomial; each polynomial is a sum of monomials; each monomial becomes one vertex, with the monomial's coefficient as its factor; and each functional derivative in the expansion brings down a field, which Wick's theorem pairs with another into a propagator. What remains after the pairing is a graph.

**Three statements, and only one of them is a derivation.** The vertex is the coefficient of the monomial, times the unit of the expansion; that is a definition read off the density. The pairing of fields two at a time is Wick's theorem; that is a theorem. And the number of vertices is the power of the coupling; that is the organisation the whole method exists to obtain. The article keeps the three apart because the literature usually merges them into one sentence called *the Feynman rules*.

**The strongest objection.** *The vertex is a definition, so the stage proves nothing.* Half right. The vertex's value is a definition — it is the interaction's coefficient, and no computation produces it. What the expansion proves is that the vertex is the *same* number at every order, that its position is a single point, and that the leftover multiplicity is the symmetry factor. Those three are the content, and they are what a reader who has only the definition cannot get.

**Position.** Stage $3$ of the chain in [the hub](the-lagrangian-method-from-the-collected-lagrangian-to-the-feynman-diagram.html). It takes the factored operator of [stage $2$](the-generating-functional-and-the-exact-gaussian-the-quadratic-part-inverted-into-the-propagator.html) and hands the diagrams to [stage $4$](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html).

## The Expansion of the Exponential

**The operator is an exponential, and an exponential is a sum.** With $S_{\mathrm{int}}=\int\mathcal L_{\ge3}$ and every field replaced by $\delta/i\delta J$,

$$
\exp\Bigl(iS_{\mathrm{int}}\bigl[\tfrac{\delta}{i\delta J}\bigr]\Bigr)
=\sum_{n\ge0}\frac{1}{n!}\Bigl(i\int\mathrm{d}^{4}r\;\mathcal L_{\ge3}\bigl[\tfrac{\delta}{i\delta J}\bigr]\Bigr)^{n}.
$$

**Each term is a product of functional derivatives at possibly different points, acting on the Gaussian.** The Gaussian's value is $\exp(-\frac{i}{2}\int J\Delta J)$, and a functional derivative of it is a linear function of $J$ times a $\Delta$. So an $n$-th order term is a product of $n$ monomials, each evaluated at its own point, with every field replaced by a sum of two kinds of object: a $\Delta J$, which is an external leg, and a $\Delta$, which joins two points.

**The two kinds of object are the two kinds of line, and nothing else appears.** This is the mechanical reason the output is a graph: the expansion produces points, and it produces pairings between points, and a set of points with pairings between them is a graph.

**The factor $\frac{2\pi}{h}$ sits in the exponent and not in the vertex.** The corpus's weight is $\exp(i\theta_{\mathrm{act}})$ with $\theta_{\mathrm{act}}=\frac{2\pi}{h}\mathrm{Re}\,S$, so the general vertex carries $\frac{2\pi i}{h}$ times the monomial's coefficient. Since $\frac{2\pi}{h}=\frac{1}{\hbar}$, the corpus's exponent is the standard $S/\hbar$, and the sector articles that write $i\times$ coefficient are working in the units $\frac{h}{2\pi}=1$. This article states the general factor once and then uses those units, as the corpus's [QCD](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html) and [$\mathrm{SU}(4)$](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html) rule articles do.

## One Monomial, One Vertex

**A monomial is local, so its vertex is a point.** Let the interaction contain a monomial $c\prod_{i=1}^{m}\phi(r)$ for a single real field, with $c$ the coefficient exactly as the density writes it, sign and denominator included. The corresponding term in $iS_{\mathrm{int}}[\delta/i\delta J]$ is a product of $m$ derivatives all at the same $r$, and when they act on the Gaussian they produce a factor at $r$ and $m$ lines leaving $r$. The vertex is therefore

$$
\text{vertex}=i\,c\,M\,\times(\text{momentum conservation}),
$$

with $M$ the number of complete assignments of the monomial's $m$ field slots to the $m$ external legs. The product $cM$ is what decides whether the vertex carries the coupling or a multiple of it.

| interaction | coefficient | matchings | vertex |
|---|---|---|---|
| $-\frac{\lambda}{4!}\phi^{4}$ | $-\frac{\lambda}{24}$ | $24$ | $-i\lambda$ |
| $-\frac{\varpi_{\mathrm{cpl}}}{4}N^{2}$, four legs on one component | $-\frac{\varpi_{\mathrm{cpl}}}{4}$ | $24$ | $-6i\varpi_{\mathrm{cpl}}$ |
| $-\frac{\varpi_{\mathrm{cpl}}}{4}N^{2}$, two legs on each of two components | $-\frac{\varpi_{\mathrm{cpl}}}{4}$ | $8$ | $-2i\varpi_{\mathrm{cpl}}$ |

**The matching counts were computed, not guessed.** Differentiating $N^{2}$ four times symbolically on the corpus's own field, with $N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ written as a sum of eight real squares, gave $24$ for four legs on one component, $8$ for two legs on each of two components and $8$ for the crossed assignment. The fourth derivative of $\phi^{4}$ is $24$. The three rows are one rule and not three conventions.

**The corpus's $\frac14$ is fixed by the equation of motion, and the vertex inherits the consequence.** [The Lagrangian and the Interacting Scalar Field](the-lagrangian-and-the-interacting-scalar-field.html) chooses $\frac{\varpi_{\mathrm{cpl}}}{4}$ so that the field equation's right side carries $\varpi_{\mathrm{cpl}}$ and not $2\varpi_{\mathrm{cpl}}$. The vertex is whatever the matching count then gives, which for four legs on one component is $-6i\varpi_{\mathrm{cpl}}$. A density written $-\frac{\varpi_{\mathrm{cpl}}}{24}N^{2}$ would give the vertex $-i\varpi_{\mathrm{cpl}}$ and the equation's right side $\frac{\varpi_{\mathrm{cpl}}}{6}N\tilde\Xi$; the two normalisations cannot be chosen independently, and this is the one place where the corpus's classical convention shows through into the diagrams.

## The Pairing Is Wick's Theorem

**Wick's theorem is the statement that a Gaussian's moments are the sum over pairings.** For a Gaussian of covariance $\Delta$,

$$
\bigl\langle\phi(r_{1})\cdots\phi(r_{2n})\bigr\rangle_{0}
=\sum_{\text{pairings}}\prod_{\text{pairs}}\Delta(r_{i}-r_{j}),
$$

and every odd moment vanishes. [The Wick Theorem in Biquaternionic Form](the-wick-theorem-in-biquaternionic-form.html) states the theorem, the fermionic sign, and the one-mode identity that closes exactly inside $\mathbb{B}$.

**The sum over pairings is the sum over diagrams, and the correspondence is one-to-one.** A pairing of the fields is a set of lines; the points at which the fields sat are the vertices; and the external legs are the unpaired fields that the source derivatives supplied. A diagram is a pairing drawn.

**The $1/n!$ and the $n!$ orderings cancel, and the leftover is the symmetry factor.** The expansion's $\frac{1}{n!}$ divides by the order of the vertices; a generic diagram is counted $n!$ times, once per ordering of its vertices, so the two cancel and the diagram's coefficient is one. A diagram with symmetries is counted fewer than $n!$ times, and the leftover is the symmetry factor: $n!$ divided by the diagram's automorphism count. The factor is a property of the graph, not of the field, and it is why the same vertex produces a factor $\frac12$ in one topology and $1$ in another.

**The fermionic sign is a scalar and not an operator.** Every exchange of two fermionic fields in the pairing contributes $-1$, and the sign multiplies the diagram. [The Wick Theorem](the-wick-theorem-in-biquaternionic-form.html) records that the sign comes from the grading of the module and not from an extra convention; the corpus's [three-diagram article](three-diagrams-of-the-su4-model-the-kaon-the-proton-chain-and-a-gluon-exchange.html) draws diagrams in which it is explicit.

## The Count of Vertices Is the Power of the Coupling

**The organisation the method exists to obtain is one line long.** If every monomial of $\mathcal L_{\ge3}$ carries one power of a coupling $g$, then a term with $n$ factors of $S_{\mathrm{int}}$ has $n$ vertices and order $g^{n}$. The series is therefore ordered by graphs and not by powers of the field.

| diagram | vertices | order | what it is |
|---|---|---|---|
| one propagator | $0$ | $1$ | free propagation |
| two vertices joined | $2$ | $g^{2}$ | tree-level scattering |
| one closed loop at one vertex | $1$ | $g$ | the first quantum correction to the mass |
| $L$ loops, $n$ vertices | $n$ | $g^{n}$ | the quantum corrections at that order |

**The table's second row is the one that corrects the usual misreading.** A four-point interaction is one vertex, so a $2\to2$ process at tree level is order $g$ and not order $g^{4}$. The degree of the monomial is four; the order in the coupling is one. The method's whole efficiency is that the second number, not the first, organises the sum.

**Loops and vertices are independent counts, and that is why the loop expansion is a different organisation.** The number of loops is $L=I-V+1$ for a connected graph with $I$ internal lines and $V$ vertices, so a fixed order in the coupling is a fixed $V$ and a variable $L$. [The fourth article](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html) uses the relation to order the diagrams, and [the sixth](the-classical-limit-of-the-diagram-series-tree-diagrams-as-the-stationary-phase-of-the-path-integral.html) uses it to count powers of the action quantum.

## What the Algebra Supplies Here

**This stage is where the corpus's ledger is thinnest, and the article says so.**

| what the stage needs | where it comes from |
|---|---|
| the monomials and their coefficients | the density, [stage $0$](the-collection-of-lagrangian-components-the-full-action-as-the-input-to-perturbation-theory.html) |
| the pairing, and the fermionic sign | the algebra, the grading of the module, [the Wick article](the-wick-theorem-in-biquaternionic-form.html) |
| the one-mode exactness of the identity | the algebra, [the Wick article](the-wick-theorem-in-biquaternionic-form.html) |
| a vertex native to $\mathbb{B}$ | nothing: the vertex is the interaction's coefficient, and the corpus's interactions are imported |
| the Standard Model's vertex list | not the algebra: [the quantisation hub](the-quantisation-hub-the-sixteen-articles-that-import-the-promotion.html) is the ledger |

**The vertex is not an algebraic object, and pretending otherwise would be the section's one overclaim.** The algebra hosts the pairing and grades the sign. The vertex is a number read from a density, and every density beyond the corpus's own scalar quartic is imported. A reader who wants the vertex list of the strong sector will find it transcribed in [The Feynman Rules of the $\mathrm{SU}(4)$ Model](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html), with the imported half marked.

## Summary

**Stage $3$ expands the interaction and pairs the fields.** Each factor of $S_{\mathrm{int}}$ costs one power of the coupling; each monomial becomes one local vertex with the monomial's coefficient; each functional derivative brings down a field; and Wick's theorem sums over the pairings, which are the lines.

**One rule covers every vertex.** The vertex is $i$ times the coefficient times the number of complete matchings, and the matching count is what the coefficient's denominator divides. Differentiating the corpus's $N^{2}$ four times gave $24$ matchings for four legs on one component and $8$ for two legs on each of two; the corresponding vertices are $-6i\varpi_{\mathrm{cpl}}$ and $-2i\varpi_{\mathrm{cpl}}$. The $\frac14$ in the corpus's density is fixed by the field equation, and the vertex inherits its consequence.

**The $1/n!$ cancels the vertex orderings and leaves the symmetry factor.** The fermionic sign is a scalar from the grading. And the number of vertices is the order in the coupling, so a quartic is order one and not order four.

## Summary of Notation

| symbol | meaning |
|---|---|
| $S_{\mathrm{int}}$ | $\int\mathcal L_{\ge3}$ |
| $c$ | the coefficient of an interaction monomial |
| $m$ | the degree of the monomial, equal to its number of field slots |
| $n$, $V$ | the number of factors of $S_{\mathrm{int}}$, hence the number of vertices |
| $L$, $I$ | the number of loops and of internal lines, $L=I-V+1$ |
| $\Delta$ | the propagator, from stage $2$ |
| $h$ | the action quantum; the vertex carries $\frac{2\pi i}{h}$ times the coefficient in general |

## Further Reading

- [The Wick Theorem in Biquaternionic Form](the-wick-theorem-in-biquaternionic-form.html), the pairing, the sign and the one-mode identity.
- [The Lagrangian and the Interacting Scalar Field](the-lagrangian-and-the-interacting-scalar-field.html), the quartic whose coefficient this article reads as a vertex.
- [The Feynman Rules and the Diagram Expansion: Propagators, Vertices, Loops and Symmetry Factors](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html), the stage that reads the series this one produced.
- [The Feynman Rules of the $\mathrm{SU}(4)$ Model: The Vertices of the Fifteen and the Sixteen](the-feynman-rules-of-the-su4-model-the-vertices-of-the-fifteen-and-the-sixteen.html), the corpus's largest vertex list, transcribed.
- [Three Diagrams of the SU(4) Model: The Kaon, the Proton Chain and a Gluon Exchange](three-diagrams-of-the-su4-model-the-kaon-the-proton-chain-and-a-gluon-exchange.html), the diagrams drawn, with the signs and the factors explicit.
- [The Quantisation Hub: The Sixteen Articles That Import the Promotion](the-quantisation-hub-the-sixteen-articles-that-import-the-promotion.html), the ledger of what the corpus transcribes.
