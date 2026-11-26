# __The Twelve Spin Coefficients in the Null Tetrad__

## Introduction

A frame is not a theory. The null tetrad of the companion article is a choice of four legs at a point, and a connection is what a derivative needs in order to compare legs at neighbouring points. In a frame the connection appears as its coefficients, and this article writes them in the framework's tetrad, counts them three times, and derives the one piece of structure the count does not show: the twelve fall into three groups of four, and the grouping is the multiplication table $lm=\sigma m$, $ml=0$ read as a statement about derivatives.

The separation held throughout is the one the companion article established and this one must not quietly close. The algebra supplies the **home** of the coefficients — the six-real-dimensional bivector subspace it identifies with $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$ — and it supplies the tetrad in which they are resolved. It does not select a connection, so it does not produce the coefficients. A different metric-compatible connection gives different numbers on the same frame, and the algebra has nothing to say about which.

## The Count: Twenty-Four Real, Twelve Complex

The tetrad is a frame, and a connection is expressed in a frame through its coefficients. Suppose a linear connection $\vec\nabla_\Phi$ on the material sector is given, metric-compatible with $\langle\cdot,\cdot\rangle_{\natural}$; the parent article records that the algebra carries such a connection but does not select one. For tetrad legs $e_a,e_b,e_c$ define

$$
\Gamma_{abc} := (\nabla_a e_b)\cdot e_c, \qquad \nabla_a := \nabla_{e_a}.
$$

Metric compatibility, $\nabla_a(e_b\cdot e_c)=0$, gives $\Gamma_{abc}+\Gamma_{acb}=0$, so the coefficients are antisymmetric in the last two tetrad indices. For each $a$ this is a $4\times4$ antisymmetric matrix with six independent entries, the connection being real, so $\Gamma_{abc}$ has $4\times6=24$ real independent components — that is, **twelve complex** ones. These twelve complex numbers, written in the standard names, are the **spin coefficients**:

$$
\kappa,\ \sigma,\ \rho,\ \tau; \qquad \pi,\ \varsigma_{\mathrm{nps}},\ \mu,\ \jmath; \qquad \varepsilon,\ \gamma,\ \beta,\ \alpha .
$$

The first four are the contractions of $\vec\nabla_\Phi l$ with the tetrad legs,

$$
\kappa = \sum_a m_a D l_a, \qquad \sigma = \sum_a m_a \delta l_a, \qquad \rho = \sum_a m_a \bar\delta l_a, \qquad \tau = \sum_a m_a \delta l_a,
$$

where $D=\sum_a l_a\nabla_a$, $\mathcal{N}_{\mathrm{NP}}=\sum_a n_a\nabla_a$, $\delta=\sum_a m_a\nabla_a$ and $\bar\delta=\sum_a \bar m_a\nabla_a$ are the directional derivatives along the tetrad. The second four are the analogous contractions of $\vec\nabla_\Phi n$, and the last four complete the components of $\vec\nabla_\Phi l$ and $\vec\nabla_\Phi n$ along $l$ and $n$ themselves. The overall signs are convention-dependent — the literature does not agree on them, and the definitions are stated here only to fix the pattern — but the count and the identification of the twelve as components of one connection are not.

In the framework the connection is valued in the bivector subspace. The parent article identifies the Lorentz Lie algebra $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$ with the six-dimensional subspace $\{\vec G : \mathrm{Sc}(\vec G)=0\}$ — equivalently, under the matrix realization, the traceless $2\times2$ matrices — spanned by $\vec e_x,\vec e_y,\vec e_z$ and $i\vec e_x,i\vec e_y,i\vec e_z$, which is the complex-pure-vector subspace of $\mathbb{B}$. A connection 1-form takes values in that subspace and has one component per tetrad direction, giving

$$
\underbrace{6}_{\text{real dim } \mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}} \ \times\ \underbrace{4}_{\text{tetrad directions}} \ =\ 24 \ \text{real}\ =\ 12 \ \text{complex},
$$

the same count as the antisymmetry of $\Gamma_{abc}$ gave. The biquaternionic statement of the spin coefficients is therefore: **they are the components, in the null tetrad, of an $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$-valued 1-form** — a $\mathbb{B}$-valued connection, since the bivectors sit inside $\mathbb{B}$.

The third count is the arithmetic of the two arithmetic identities above read backwards. The antisymmetry leaves six real numbers per leg, and the bivector has six real dimensions; that the two sixes agree is not a coincidence but the statement that a metric-compatible connection is a bivector-valued 1-form, and it is the reason the twelve complex spin coefficients and the twenty-four real $\Gamma_{abc}$ are the same object in two notations.

## The Four Directional Derivatives

The tetrad legs act as derivations, and the four operators

$$
D = \sum_a l_a\nabla_a, \qquad \mathcal{N}_{\mathrm{NP}} = \sum_a n_a\nabla_a, \qquad \delta = \sum_a m_a\nabla_a, \qquad \bar\delta = \sum_a \bar m_a\nabla_a
$$

are not a coordinate basis: they are the four legs of a complex null frame, and six commutators among them are the complete statement that the frame does not integrate to coordinates. Each commutator is again a directional derivative, and its coefficients are spin coefficients — that is the reason the twelve names are the natural vocabulary of the formalism rather than an arbitrary list. Two consequences follow and are used in every application. First, a scalar field's second derivatives computed in two orders differ by spin-coefficient terms, so the formalism carries its own integrability conditions. Second, the direction of $l$ is the direction in which the algebra's own $D$ derivative is taken, and the algebra never needs the other three: $D$ alone is the derivative along the idempotent leg.

Here the framework adds a remark that is about the algebra and not about the coefficients. The four legs are the matrix units, so $D$ is the derivative along $\tilde\Pi_{\mathrm{id},1}$, $\delta$ along $x$, $\bar\delta$ along $y$, and $\mathcal{N}_{\mathrm{NP}}$ along $\tilde\Pi_{\mathrm{id},2}$; the four derivatives are the four Peirce corners read as directions. The four are the same objects whether or not a connection is chosen — the choice enters only in the coefficients, not in the directions.

## The Weight Rule

The twelve transform among themselves under the six-parameter tetrad rotation, and the transformation is diagonal in the boost–spin direction. The weights are not memorised: they are counted, and the count is a rule.

Each spin coefficient is a contraction of one gradient with two legs. Assign to each gradient the weight of the leg it differentiates,

$$
\nabla l \sim (1,0), \qquad \nabla n \sim (-1,0), \qquad \nabla m \sim (0,1), \qquad \nabla\bar m \sim (0,-1),
$$

and to each leg the weight of its own scaling under $l\mapsto A l$, $n\mapsto A^{-1}n$, $m\mapsto e^{i\theta_{\mathrm{cen}}}m$,

$$
l \sim (1,0), \qquad n \sim (-1,0), \qquad m \sim (0,1), \qquad \bar m \sim (0,-1) .
$$

The weight of the coefficient is the sum of the three, first entry for the boost $A$ and second for the spin $e^{i\theta_{\mathrm{cen}}}$. The rule reproduces every standard weight, and four examples are enough to check it:

| coefficient | contraction | weights summed | boost, spin |
| --- | --- | --- | --- |
| $\kappa$ | $\nabla l$, $m$, $l$ | $(1,0)+(0,1)+(1,0)$ | $2,\,1$ |
| $\sigma$ | $\nabla l$, $m$, $m$ | $(1,0)+(0,1)+(0,1)$ | $1,\,2$ |
| $\rho$ | $\nabla l$, $m$, $\bar m$ | $(1,0)+(0,1)+(0,-1)$ | $1,\,0$ |
| $\tau$ | $\nabla l$, $m$, $n$ | $(1,0)+(0,1)+(-1,0)$ | $0,\,1$ |

The four coefficients of $\nabla n$ come out negative in the boost, as they must: $\pi$ weighs $(0,-1)$, $\mu$ weighs $(-1,0)$, $\varsigma_{\mathrm{nps}}$ weighs $(-1,-2)$, and $\jmath$ weighs $(-2,-1)$. The four mixed coefficients weigh $\varepsilon(1,0)$, $\gamma(-1,0)$, $\beta(0,1)$ and $\alpha(0,-1)$; $\varepsilon$ and $\gamma$ are real, $\alpha$ and $\beta$ complex, which is why the mixed group is four real numbers and not four complex ones.

The rule matters because it turns a table into a derivation. The twelve are the contractions of two gradients with pairs of legs, the legs have known weights, the gradients have the weights of the legs they differentiate, and the three groups of four are the three possible source-and-target combinations. Nothing here depends on the algebra; what depends on the algebra is that the legs *have* these weights at all, because they are the matrix units and the boost acts on them by scalar multiplication.

## Where the Two Quadruples Come From

The multiplication table of the companion article contains an asymmetry, $lm=\sigma m$ while $ml=0$, and it is the algebraic reason the twelve do not form a symmetric set.

Left multiplication by $l$ keeps $m$; right multiplication kills it. The same asymmetry holds throughout the table: $l\bar m=0$ while $\bar ml=\sigma\bar m$, and $nm=0$ while $mn=\sigma m$. So the two real legs are not interchangeable, and no operation of the algebra carries the $l$-corner to the $n$-corner. In the table the four coefficients built on $\nabla l$ and the four built on $\nabla n$ therefore have no algebraic relation to one another; the only thing that relates the two blocks is the bilinear form, which pairs $l$ with $n$ and is what a boost preserves.

That is why the boost is not an automorphism of the algebra and the twelve are not organised into six pairs. The boost, $l\mapsto A l$ with $n\mapsto A^{-1}n$, preserves the form and preserves the multiplication table's structure, but it acts on the two real corners by reciprocal scalars — it is an automorphism of the algebra only at $A=1$. The trace does not help either: $\mathrm{tr}\,\tilde\Pi_{\mathrm{id},1}=\mathrm{tr}\,\tilde\Pi_{\mathrm{id},2}=1$, so the two idempotent corners are indistinguishable by trace and are distinguished only by their position in the table. **The two quadruples of spin coefficients are the two idempotent corners of the multiplication table, and the asymmetry of the table is why they are two quadruples rather than one octet.**

## Flat Space, and What the Coefficients Measure

In flat spacetime with the constant tetrad of the companion article, every $\vec\nabla_\Phi e_a$ vanishes and all twelve coefficients are zero. That is the calibration: the coefficients are not intrinsic to a point, they are the failure of the frame to be covariantly constant.

Three readings of that failure are worth separating, because the literature uses all three and they are not the same statement. The coefficients are the **connection in the frame** — the twenty-four real numbers $\Gamma_{abc}$ in another notation. They are the **non-integrability of the frame** — the six commutators of the four directional derivatives, which vanish exactly when the frame is a coordinate frame, and which vanish for the constant tetrad above. And on a null congruence they are the **optical scalars**: $\rho$ is the expansion and $\sigma$ the shear of the congruence of $l$, in the sense that their real and imaginary parts give the divergence and the shear of the ray family. The first reading is the definitional one, the second explains why the same twelve appear in commutators, and the third is the one that carries physical content.

The third reading is where the framework's null structure pays. Expansion and shear are properties of a family of the algebra's zero divisors, so they describe the congruence of a **null direction field** that the algebra already names, and they do so at the level of the derivative along that field. Nothing in the definition of $\rho$ and $\sigma$ needs an orthonormal frame; the whole apparatus is native to the null basis, which is the reason the formalism was built on it.

## Goldberg–Sachs, and the Limit of the Account

One theorem links this article to the next, and it is the cleanest statement of what the algebra does and does not do.

**Goldberg–Sachs.** In a spacetime satisfying the vacuum Einstein equations — more generally, in any Einstein space — a null congruence is geodesic and shear-free if and only if the Weyl scalar $\tilde{Ξ}_{0}$ vanishes in the tetrad adapted to it.

The theorem is a theorem of Newman–Penrose analysis, established in 1962, and it is not derived here. Its two sides are both objects the algebra hosts: the hypothesis is $\kappa=0$ and $\sigma=0$, two of the twelve coefficients of this article; the conclusion is $\tilde{Ξ}_{0}=0$, one of the five scalars of the next. What the framework contributes is not the implication but the fact that hypothesis and conclusion are read in one frame — the same tetrad that makes $l$ a matrix unit makes $\kappa$ and $\sigma$ its derivatives and makes $\tilde{Ξ}_{0}$ the contraction of the curvature with it.

What the framework does not contribute is the implication itself, and the reason is the same as everywhere else in this section: the coefficients depend on a connection the algebra does not select, and the scalar depends on a curvature the algebra does not determine. Goldberg–Sachs is a statement about the pair of them, and a statement about the pair cannot come from an algebra that supplies neither member.

## What the Count Does Not Give

Three things are absent, and they are absent in the same way.

The **connection** is not selected, so the twelve numbers are not produced. The algebra supplies the bivector in which they take their values and the tetrad in which they are read; a metric gives the rest, and the metric is external.

The **field equations** are not present, so the coefficients are not constrained. In general relativity the twelve and the five are tied by the Bianchi identities and the field equations, and those identities are where the physical content of the formalism lives. Nothing in the algebra imposes them.

The **global structure** is not present, so no statement about a congruence over a manifold follows. Geodesic completeness, the formation of caustics, the peeling of the scalars at infinity — all are statements about limits, and the algebra is pointwise.

The accounting is therefore the same as for the tetrad itself, one level up. The algebra hosts the vocabulary — the bivector, the tetrad, the four derivatives, the weights. It does not host the sentence written in that vocabulary, and the sentence is the physics.
