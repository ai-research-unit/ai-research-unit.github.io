# __Projections of a Fractal and the Dimension__

## Introduction

The **orthogonal projection** of a fractal onto a line is the first test of the set against a linear map. For $E \subseteq \mathbb{R}^2$ and a unit vector $u_\theta = (\cos\theta,\sin\theta)$ the projection is the map $\pi_\theta(x) = x \cdot u_\theta$, a linear contraction of norm one, so it can only lower the dimension: $\dim_H \pi_\theta(E) \leq \min(\dim_H E, 1)$ for every direction. The content of the theory is that the inequality is an equality in almost every direction. This is the **projection theorem** of Marstrand: for a Borel set of dimension $s$, the projection onto the line of angle $\theta$ has dimension $\min(s,1)$ for almost every $\theta$, and has positive length for almost every $\theta$ when $s > 1$. The exceptional directions are the places where the fractal is aligned with the projection, as the axes are for a product set, and their smallness — of measure zero, and of controlled dimension — is the quantitative form of the theorem. The general theorem for the $m$-planes of $\mathbb{R}^n$ is that of Mattila.

The projection is also an **operator**: it acts on the measures carried by the fractal by pushforward, it has an adjoint, the inclusion of the line, and the theorem is proved by averaging the energy of the pushed measure over the family of the projections. The measure-theoretic form of the statement — the projection of a measure, the energy method and the **slicing** theorem for the sections of a set by a line — belongs to *Geometric Measure Theory* of the analysis part, where the Frostman lemma and the differentiation theory are available, and is cited from there; what belongs here is the operator framing, the behaviour of the **fractional** dimensions, the census of the **exceptional directions** and the sharpness, and the reduction of the **distance-set** problem to the projections, which is the subject of *The Distance Set of a Fractal*.

This article defines the projection as a linear operator and its pushforward on measures, with the adjoint inclusion; states the Marstrand and Mattila projection theorems and the energy identity that proves them; analyses the exceptional set of directions, with the bounds of Kaufman, Falconer, Oberlin and Bourgain and the sharp examples of Kenyon; states the slicing theorem and its duality with the projection; and reduces the distance set to the radial projections of the difference set. The examples are computed on the standard self-similar sets: the product of two middle-thirds Cantor sets, the four-corner Cantor set and the one-dimensional Sierpiński gasket.

The article assumes *Metric Geometry* for the distance, the diameter and the Lipschitz conditions; *Fractal Geometry* for the covering numbers, the Hausdorff content, the dimension and the self-similar sets; *Geometric Measure Theory* for the $s$-energy of a measure, the Frostman lemma, the projection and slice theorems, the rectifiability criteria and the projection criterion of Besicovitch and Marstrand; and *Measure Theory and Integration* for the Fubini theorem and the Lebesgue measure. The distance set itself is *The Distance Set of a Fractal*. No physics is invoked.

## The Projection as a Linear Operator

**Definition.** For a unit vector $u \in \mathbb{R}^n$ the **orthogonal projection** onto the line $\mathbb{R}u$ is the linear map $\pi_u(x) = (x \cdot u)\,u$, identified with the scalar $x \cdot u \in \mathbb{R}$; for an $m$-dimensional subspace $V$ the orthogonal projection is $\pi_V$, the restriction to $V$ of the orthogonal decomposition. The projection is linear, surjective, of operator norm one, and it does not increase any distance: $|\pi_V x - \pi_V y| \leq |x - y|$.

**Definition (the pushforward and the adjoint).** For a finite Borel measure $\mu$ on $\mathbb{R}^n$ the **pushforward** $\pi_{V\#}\mu$ is the measure on $V$ defined by

$$
\int_V f\,d(\pi_{V\#}\mu) = \int_{\mathbb{R}^n} (f \circ \pi_V)\,d\mu
$$

for every continuous $f$; the support of $\pi_{V\#}\mu$ is $\pi_V(\operatorname{supp}\mu)$. Under the identification of a measure with the functional $f \mapsto \int f\,d\mu$, the map $\mu \mapsto \pi_{V\#}\mu$ is the transpose of the pullback $f \mapsto f\circ\pi_V$, and on the Euclidean spaces the Hilbert-space adjoint of $\pi_V : \mathbb{R}^n \to V$ is the **inclusion** $V \hookrightarrow \mathbb{R}^n$. The projection is a contraction and the inclusion is an isometry; the pair is the operator form of the statement that the projection can lower the dimension and the inclusion cannot.

**Theorem (the monotonicity of the dimensions).** For $E \subseteq \mathbb{R}^n$ and every subspace $V$,

$$
\dim_H \pi_V E \leq \min(\dim_H E, \dim V) , \qquad \dim_B \pi_V E \leq \min(\dim_B E, \dim V) ,
$$

and similarly for the packing dimension. The dimension of a Lipschitz image is at most that of the set, by the Hölder rule of *Fractal Geometry*, and the projection lies in $V$.

**Proof sketch.** A Lipschitz map of constant one does not increase the diameter of a cover, so the covering content of the image is at most that of the set; the ambient subspace contributes the bound $\dim V$. The box and packing dimensions obey the same covering estimate.

**Remark (the operator norm and the obstruction).** The inequality is the failure of the projection to be an isometry on the directions inside $V$: two points differing only by a vector orthogonal to $V$ are sent to the same point of $V$, and the whole question of the theory is how much of the set can be concentrated in the fibres. The energy identity of the theorem below says that this concentration is invisible to the average over the directions.

## The Projection Theorems of Marstrand and Mattila

**Theorem (Marstrand, 1954).** Let $E \subseteq \mathbb{R}^2$ be Borel or analytic, with $\dim_H E = s$. Then for almost every $\theta \in [0,\pi)$

$$
\dim_H \pi_\theta E = \min(s, 1) ; \qquad \text{if } s > 1 \text{ then } \bigl|\pi_\theta E\bigr| > 0 ,
$$

where $|\cdot|$ is the Lebesgue measure.

**Theorem (Mattila, 1975).** Let $E \subseteq \mathbb{R}^n$ be Borel or analytic, with $\dim_H E = s$, and let $G(n,m)$ be the Grassmannian of the $m$-dimensional subspaces. Then for almost every $V \in G(n,m)$

$$
\dim_H \pi_V E = \min(s, m) ; \qquad \text{if } s > m \text{ then } \mathcal{H}^m(\pi_V E) > 0 .
$$

**Proof sketch (the energy identity).** The engine is the identity, valid for $0 < t < n$ and due to the rotational symmetry of the sphere,

$$
\int_{S^{n-1}} \bigl|u \cdot w\bigr|^{-t}\,du = c_{n,t}\,\bigl|w\bigr|^{-t} ,
$$

with a constant $c_{n,t}$ depending only on $n$ and $t$. If $E$ carries a measure $\mu$ of finite $t$-energy, $\mathcal{I}_t(\mu) = \iint |x-y|^{-t}\,d\mu\,d\mu < \infty$, then the identity with Fubini gives

$$
\int_{S^{n-1}} \mathcal{I}_t(\pi_{u\#}\mu)\,du = c_{n,t}\,\mathcal{I}_t(\mu) < \infty ,
$$

so the projected measure has finite $t$-energy for almost every direction, and hence the projection has dimension at least $t$ for almost every direction. Choosing $t < \min(s,m)$ and letting $t$ increase gives the lower bound; the upper bound is the contraction. The positive-measure statement follows from the finiteness of the energy at $t = m$ and the density theorem. The argument is the one of *Geometric Measure Theory*, where the energy, the Frostman lemma and the projection of a measure are constructed; the statement above is the dimension form.

**Remark (the regularity hypothesis).** The theorem requires the set to be Borel or analytic. For an arbitrary set the conclusion can fail: assuming the continuum hypothesis there is a plane set of Hausdorff dimension one whose every orthogonal projection has dimension zero, a counterexample to the unqualified statement due to Davies. The regularity is therefore not a technical convenience but a necessary hypothesis, and it is the reason the corpus works with the Borel and analytic sets of *Descriptive Set Theory*.

**Example (the product of two Cantor sets, computed).** Let $E = C \times C \subseteq \mathbb{R}^2$ with $C$ the middle-thirds Cantor set, so $s = 2\log2/\log3 = 1.2619\ldots > 1$. The projection onto the horizontal axis is the first factor, $C$, of dimension $\log2/\log3 = 0.6309\ldots$, strictly less than $s$; the projection onto the diagonal, $\theta = \pi/4$, is the sumset scaled by $1/\sqrt2$, which fills the interval $[0,\sqrt2]$ of dimension one, equal to $\min(s,1)$. At the first levels of the construction the effect is visible: the set $C_k \times C_k$ has $4^k$ squares, and its horizontal projection has $2^k$ intervals of total length $(2/3)^k$, tending to zero, while its diagonal projection is a single interval of length $\sqrt2$ already at the level $k = 1$. The horizontal and the vertical directions are exceptional; the diagonal is typical.

**Example (the one-dimensional Sierpiński gasket, Kenyon).** The **one-dimensional Sierpiński gasket** is the self-similar set of the three maps of ratio $\frac13$ fixing the corners $(0,0)$, $(\frac23,0)$ and $(0,\frac23)$ of the unit square; its dimension is $\log3/\log3 = 1$. By the theorem of Kenyon, the projection onto a rational direction of slope $p/q$ has positive measure exactly when $p+q \equiv 0 \pmod 3$, and has dimension strictly less than one otherwise, while the projection onto an irrational direction is null but has Hausdorff dimension one, the latter by the theorem of Hochman. The set exhibits, in a single self-similar object, a countable family of exceptional directions with positive measure, and a full-measure family with null projections of full dimension.

**Example (the gasket projects to an interval in every direction).** The standard Sierpiński gasket, the attractor of three maps of ratio $\frac12$ at the vertices of an equilateral triangle, is connected and contains the three vertices; its projection onto any line is therefore a compact connected subset of the line realising the extreme projected vertices, that is an interval. The dimension of every projection is one, the maximum allowed by $\min(s,1)$ with $s = \log3/\log2 = 1.5850\ldots$; and the length of the interval varies with the direction, being $1$ for the horizontal and for the directions of the three sides and $\sqrt3/2 = 0.8660\ldots$ for the vertical. The example is the extreme case in which the projection theorem is trivially sharp.

## The Exceptional Set of Directions

**Definition.** For $0 \leq t \leq \dim_H E$ let

$$
\Theta_t(E) = \{\theta \in [0,\pi) : \dim_H \pi_\theta E < t\}
$$

be the set of the directions in which the projection is smaller than the threshold $t$. Marstrand's theorem says that $\Theta_s(E)$ has Lebesgue measure zero for $s = \min(\dim_H E, 1)$.

**Theorem (the size of the exceptional set).**

**(a)** (Kaufman, 1968) If $0 < t < \dim_H E < 1$, then $\dim_H \Theta_t(E) \leq t$.

**(b)** (Oberlin; Bourgain) If $\dim_H E < 1$, then $\Theta_{\frac12\dim_H E}(E)$ has Hausdorff dimension zero: the projection has at least half the dimension of the set in almost every direction, in the full-measure sense.

**(c)** (Falconer, 1982) If $\dim_H E > 1$, then the set of the directions in which the projection has Lebesgue measure zero has Hausdorff dimension at most $2 - \dim_H E$.

**Proof sketch.** (a) is the refined reading of the energy argument of Kaufman: if the exceptional set carried a measure of dimension exceeding $t$, the integration of the energy identity against that measure would give a direction in which the projected energy is finite, contradicting the definition of the set. (b) is the improvement of the same method with the restriction of the Fourier transform of the measure to the sphere; the estimates are those of Oberlin and Bourgain. (c) is the theorem of Falconer, proved by a Fourier-transform argument; the vanishing of the Lebesgue measure of the projection is detected by the decay of the transform of the measure, and the exceptional set is controlled by the excess dimension $\dim_H E - 1$. The statements are quoted from the survey of Falconer, Fraser and Jin, and the attribution of (a) and (c) is theirs.

**Remark (reading the menu's "dimension zero").** The statement that the exceptional set of directions is *of dimension zero* is the sharpest form of the theory, and it holds for the threshold of one half when $\dim_H E < 1$ (part (b)); for the full conclusion the exceptional set is only of measure zero, and its dimension is bounded by $t$ or by $2 - \dim_H E$ according to the case. The distinction matters: for the product set $C \times C$ of the previous section the exceptional directions include the two axes, a set of dimension zero, consistent with the bound $2 - s$ of part (c); but a set of dimension $s = 1.1$ can have an exceptional set of dimension up to $0.9$, which is far from zero.

**Remark (the sharpness).** The bounds are sharp: the one-dimensional Sierpiński gasket has positive-measure projections in a countable family of rational directions and null projections in all the irrational directions of full dimension, so the exceptional set of part (c) is nonempty and, for a suitable self-similar set with a large rotation group, of the dimension allowed by the bound. When the rotation group of the iterated function system is finite, the projections in the directions aligned with the images of the pieces coincide, and the reduction of the dimension is exact; this is the mechanism behind all the examples. The survey's discussion of the alignment of the component squares is the general form of the computation.

## The Slicing Theorem

**Theorem (slicing; Marstrand and Mattila).** Let $E \subseteq \mathbb{R}^n$ be Borel with $\dim_H E = s$, and let $0 \le m < n$. Then for almost every $(n-m)$-dimensional subspace $W$ and almost every $x$,

$$
\dim_H \bigl(E \cap (x + W)\bigr) \leq \max(0, s - m) ,
$$

and for a set of translates of positive measure the inequality is an equality when $s > m$; equivalently, in the plane, a set of dimension $s > 1$ meets almost every line in a set of dimension at most $s-1$, with equality for a positive-measure set of lines.

**Proof sketch.** The statement is the Fubini-type dual of the projection theorem: the slicing is the disintegration of the measure by the projection, the growth condition of the Frostman measure on the set controls the growth of the conditional measures on the slices, and the integration over the translates gives the bound; the equality on a positive-measure set of slices follows from the same energy estimate at the critical exponent. The proof is that of *Geometric Measure Theory*, where the Frostman lemma and the projection theorem are proved together.

**Example (the slices of the product set).** For $E = C \times C$ the vertical line at $x$ meets $E$ in the vertical copy of $C$ when $x \in C$ and in the empty set otherwise, so the slice has dimension $\log2/\log3 = 0.6309\ldots$ for a set of $x$ of dimension $0.6309\ldots$ and is empty otherwise. The slicing bound at the exponent $s - 1 = 0.2619$ would be violated by the vertical slice, and there is no contradiction: the vertical direction is one of the exceptional directions of measure zero in which the projection is small, so the theorem — which is a statement about almost every direction and almost every line — does not apply to it. This is the sharpest illustration of the interplay between the projection and the slice: the direction must be typical for both.

**Remark (why the two theorems are one).** The projection and the slicing are the two halves of the same disintegration. The projection theorem says that the image of a measure is large for almost every direction; the slicing theorem says that the fibres of the projection are small. The identity behind both is the Fubini theorem for the measure of *Measure Theory and Integration*, and the two counts are the two sides of the same integral identity. In the language of the operator of the first section, the pushforward controls the image and the conditional measures control the kernel.

## The Application to the Distance Set

**Definition.** The **distance set** of $E \subseteq \mathbb{R}^n$ is $\Delta(E) = \{|x-y| : x, y \in E\}$, and the **difference set** is $E - E = \{x - y : x,y \in E\}$.

**Reduction.** The distance set is the image of the difference set under the radial map, and the radial map is the projection of the difference set along the direction of the difference:

$$
|x - y| = \pi_{u}(x-y) \quad \text{for} \quad u = \frac{x-y}{|x-y|} .
$$

So the distance set is the union, over the directions, of the projections of the difference set onto those directions, and a lower bound on the size of the projections in a large set of directions gives a lower bound on the distance set. The projection theorem of this article is thus the geometric input of the **Falconer distance problem**, and the threshold is read off from the dimension of the difference set, which is at least the dimension of $E$ because for a fixed $x \in E$ the translate $x - E$ is isometric to $E$ and is contained in $E - E$. The precise form of the implication, the Falconer threshold $\dim_H E > \frac{n}{2}$ and the partial results, are the subject of *The Distance Set of a Fractal*, where the arithmetic of the distance set is also treated.

**Remark (the difference set and the energy).** The difference set $E - E$ has dimension at least $\dim_H E$: for a fixed $x \in E$ the translate $x - E$ is an isometric copy of $E$ contained in $E - E$, so the dimension cannot drop. The Falconer theorem then asks, in addition, for the *measure* of the set of the realised distances, which the dimension alone does not supply. This is why the projection theorem is not by itself sufficient and the Fourier analysis of the spherical average enters.

## Summary

The orthogonal projection of a fractal onto a line is a linear contraction of norm one, so it cannot increase the dimension, and the projection theorem of Marstrand and Mattila says that for almost every direction it realises the maximum $\min(\dim_H E, m)$ and, when the dimension exceeds $m$, gives a projection of positive measure. The proof is the energy identity that averages the energy of the projected measure over the directions, and it requires the set to be Borel or analytic. The exceptional directions have measure zero and their dimension is controlled by the theorems of Kaufman, Falconer, Oberlin and Bourgain, the sharpest of which makes the exceptional set zero-dimensional at the half-dimension threshold; the sharp examples are the self-similar sets with a finite rotation group, of which the one-dimensional Sierpiński gasket of Kenyon is the detailed case, with positive-measure projections exactly in the rational directions of slope $p/q$ with $p + q \equiv 0 \pmod 3$ and null projections of full dimension in the irrational directions. The slicing theorem bounds the dimension of the sections of a set by a line by $\dim_H E - 1$, and the two theorems are the two halves of the disintegration of the measure by the projection. The distance set is the radial image of the difference set, and the projection theorem is the geometric input of the Falconer problem treated in *The Distance Set of a Fractal*. The measure-theoretic form of the projection and slicing theorems, with the Frostman lemma and the projection criterion of Besicovitch and Marstrand, is that of *Geometric Measure Theory*, and the dimension is that of *Fractal Geometry*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi_V$, $\pi_\theta$ | Orthogonal projection onto the subspace $V$, onto the line of angle $\theta$ |
| $\pi_{V\#}\mu$ | Pushforward of the measure $\mu$; the inclusion is the adjoint of $\pi_V$ |
| $G(n,m)$ | Grassmannian of the $m$-dimensional subspaces of $\mathbb{R}^n$ |
| $\mathcal{I}_t(\mu)$, $s$-energy | $\iint\lvert x-y\rvert^{-t}d\mu\,d\mu$; the finiteness bounds the dimension below |
| $\Theta_t(E)$ | The set of directions in which $\dim_H\pi_\theta E < t$ |
| $\min(s,m)$ | The generic dimension of the projection of an $s$-set |
| $s-m$ | The slicing bound for the sections by an $(n-m)$-dimensional subspace |
| $C\times C$, $\log2/\log3$ | Product of two Cantor sets; the exceptional directions are the axes |
| One-dimensional Sierpiński gasket | Three maps of ratio $1/3$; Kenyon's example |
| $\Delta(E)$, $E-E$ | Distance set; difference set, $\Delta$ is the radial image of $E-E$ |

## Further Reading

- John M. Marstrand, "Some fundamental geometrical properties of plane sets of fractional dimensions", *Proceedings of the London Mathematical Society* (3) 4 (1954), 257–302, for the projection and slice theorems.
- Pertti Mattila, "Hausdorff dimension, orthogonal projections and intersections with planes", *Annales Academiae Scientiarum Fennicae A Math.* 1 (1975), 227–244, for the general $m$-plane theorem and the slices.
- Pertti Mattila, *Geometry of Sets and Measures in Euclidean Spaces* (Cambridge University Press, 1995), for the energy method, the Frostman lemma and the proofs.
- Robert Kaufman, "On Hausdorff dimension of projections", *Mathematika* 15 (1968), 153–155, and Kenneth J. Falconer, "Hausdorff dimension and the exceptional set of projections", *Mathematika* 29 (1982), 109–115, for the exceptional sets of directions.
- Roy O. Davies, "Two counterexamples concerning Hausdorff dimensions of projections", *Colloquium Mathematicum* 42 (1979), 53–58, for the failure of the projection theorem for non-analytic sets.
- Daniel M. Oberlin, "Restricted Radon transforms and projections of planar sets", *Canadian Mathematical Bulletin* 55 (2012), 136–141, and Jean Bourgain, "On the Erdős–Volkmann and Katz–Tao ring conjectures", *Geometric and Functional Analysis* 13 (2003), 334–365, for the half-dimension threshold.
- Kenneth Falconer, Jonathan Fraser and Xiong Jin, "Sixty years of fractal projections", in *Fractal Geometry and Stochastics V* (Progress in Probability 70, 2015), 3–25, for the survey of the whole circle of ideas.
- Richard Kenyon, "Projecting the one-dimensional Sierpiński gasket", *Israel Journal of Mathematics* 97 (1997), 221–238, and Michael Hochman, "On self-similar sets with overlaps and inverse theorems for entropy", *Annals of Mathematics* 180 (2014), 773–822, for the exact projections of the gasket.
