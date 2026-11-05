# __Frame and Metric Conventions__

## Introduction

In this article a *frame* means a spacetime frame: a choice of coordinates on the biquaternion space. There are two, the $\mathbb{B}$ frame and the $\mathbb{M}_-$ frame, and every display in the series is written in one of them. A reader who mixes the two changes a sign or a factor of $i$ and has no way to see it in the result.

**The word metric has one meaning in the series. There is one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$: diagonal, all four coefficients $+1$, the matrix of the interval $\sum_\mu Q_\mu^2$. A frame carries a coordinate, not a metric. The minus of the material sector is not a metric: it is $i^2=-1$ in $Q_t=i c r'_t$, made once on the time.**

This article fixes the general notion first, then the two coordinate frames. The $\mathbb{B}$ frame is the general frame of the biquaternion universe, and its metric is the unit metric, $\delta_{\mu\nu}=(1,1,1,1)$, the same one the two sectors carry. The $\mathbb{M}_-$ frame is a particular case of it on the material sector, kept to display familiar equations in their usual form; there the interval is $-c^2t'^2+r_x^2+r_y^2+r_z^2$, and its one minus is the square of the $i$ in $Q_t=i c r'_t$. It then gives the Clifford map, which translates those directions into $M_4(\mathbb{C})$ and is a dictionary rather than a structure of the algebra, and it closes with the rules that keep them apart.

Each frame is fixed with its coordinate. The coordinate is part of the frame, not a separate choice; there is one metric, $\delta_{\mu\nu}=(1,1,1,1)$. The plain weight belongs to the product and is the same in both frames.

The article is read after *Algebra and Element Conventions* and before *Matrix Representations Conventions*. It uses no left or right multiplication, no cell and no explicit array.

**The order is the order of dependence, and it is also the order of risk.** The coordinate frame decides the signs of every interval term. A mistake in it propagates into every display of the article that follows.

## What a Frame Is

**A frame is a choice of coordinate, not a part of the object.** It is a rule that turns an element into four labelled components, together with a stated law for passing to another such rule. The object is what the rule leaves fixed. The coordinate is part of the frame, not a choice made after it: each of the two frames carries its interval, and the two intervals differ by the one $i$ inside a coefficient, while the metric is $\delta_{\mu\nu}$ in both. The test of a frame statement is that it names the frame and its coordinate; the test of an invariant statement is that it does not. A coordinate taken from one frame and read in the other is an object of neither, and no algebraic check detects it.

**The two coordinate frames have names.** The names are read $\mathbb{B}$ for biquaternion and $\mathbb{M}_-$ for the material sector. The $\mathbb{B}$ frame is the biquaternion space read in its own complex coordinate: the natural complete frame, with no reality condition and all four directions on the same footing. The $\mathbb{M}_-$ frame is the material real frame, named for the sector it is defined on, reached by $Q_t=i c r'_t$ in physics and by $Q_t=iq'_t$ in mathematics. $Q_\mu$ stays the name of the complex coordinate and $x_\mu$ the name of the real one; the frame name and the coordinate name are separate. The four values of the map carry the index low and no frame label: they are one set of arrays, the same in both frames, and the arrays themselves are displayed in §*The Clifford Map*. The frame is named on the coordinate, $Q_\mu$ or $x_\mu$, and never on the array.

**The frame and the invariant are read together.** The plain weight is an invariant: $\mathrm{Sc}(e_t^2)=+1$ and $\mathrm{Sc}(\vec e_k^2)=-1$ hold in both frames, so $\varepsilon=(1,-1,-1,-1)$ belongs to the product and not to a frame. What a frame supplies is the coordinate, and the coordinate alone fixes the interval. There is one metric, $\delta_{\mu\nu}$, and it is the same in both frames. The weight and the metric are two objects, and no sentence needs both to be read.

**A change of frame is a substitution with a law.** On the material sector it is $Q_t=ix_0$ and $Q_k=x_k$ for $k=1,2,3$, with the inverse $x_0=-iQ_t$ and $x_k=Q_k$. A display is read only in the frame that produced it, and the substitution is written wherever a display passes from one frame to the other.

## The $\mathbb{B}$ Frame

**The coordinate is complex.** The $\mathbb{B}$ frame is the biquaternion space read in its own complex coordinate: the natural complete frame. It reads the four coefficients of the element and imposes no reality condition,
$$
\tilde Q=Q_t\,e_t+Q_x\,\vec e_x+Q_y\,\vec e_y+Q_z\,\vec e_z,\qquad Q_\mu\in\mathbb{C}.
$$
This is the general case. The two real sectors are conditions on these four coefficients, not other frames.

**The interval has four $+1$ coefficients.** With the natural conjugation $\natural$,
$$
\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural=Q_t^2+Q_x^2+Q_y^2+Q_z^2 .
$$
Every coefficient is $+1$, and the value is complex in general. The tuple is a coefficient tuple, not a real signature; a signature appears only when a sector is imposed. On $\mathbb{M}_-$, with $Q_t=i c r'_t$, the value is $-c^2t'^2+r_x^2+r_y^2+r_z^2$; on $\mathbb{M}_+$, with $Q_t=c r_t$ and $Q_k=i r'_{x_k}$, it is $c^2t^2-r'_{x}^2-r'_{y}^2-r'_{z}^2$. The metric is $\delta_{\mu\nu}=(1,1,1,1)$, and on $\mathbb{M}_-$ the interval is still the plain sum $\sum_\mu Q_\mu^2$, read on the complex coefficient $Q_t=i c r'_t$.

**The general frame, and its form is Euclidean.** The $\mathbb{B}$ frame is the frame of the biquaternion universe itself, not of one sector of it; the $\mathbb{M}_-$ frame is this one read on a sector. Its form is $\sum_\mu Q_\mu^2$, with all four coefficients $+1$. On real coefficients that is the ordinary Euclidean metric: positive definite, with no direction singled out by a sign. The coefficients are complex in general, so the form is the complexified Euclidean form; a real signature appears only when a sector is imposed. A Lorentzian signature is not a property of this frame.

**The metric is the identity, and it is the same in both frames.** It is $\delta_{\mu\nu}=(1,1,1,1)$, so the interval is the plain sum $\sum_\mu Q_\mu^2$ and no direction is singled out by a sign. No array enters the frame: the arrays belong to *Matrix Representations Conventions*, and the squares of their four values are the same in both frames. What separates the two frames is the coordinate that reads an interval, not the squares.

**The material case.** On $\mathbb{M}_-$ the coefficients are
$$
Q_t=i c r'_t,\qquad Q_x=r_x,\qquad Q_y=r_y,\qquad Q_z=r_z ,
$$
with $r'_t,r_x,r_y,r_z$ real and $c$ the local speed of light. This is the coordinate the physics corpus writes by default. It is a sector condition on the $\mathbb{B}$ frame, not the definition of the frame.

## The $\mathbb{M}_-$ Frame

**The coordinate.** The $\mathbb{M}_-$ frame is the material coordinate, defined on $\mathbb{M}_-$,
$$
x_0=c r'_{t},\qquad x_1=r_x,\qquad x_2=r_y,\qquad x_3=r_z ,
$$
with $r'_t,r_k$ real. On the material case $Q_t=ix_0$ and $Q_k=x_k$ for $k=1,2,3$: one substitution, a rotation of the time axis by $i$.

**A particular case, kept for convenience.** The $\mathbb{M}_-$ frame is the $\mathbb{B}$ frame restricted to $\mathbb{M}_-$, not a second universe and not a second algebra. It is defined only after the coefficients have been put on that sector, and its one change is the time coordinate: $Q_t=i c r'_t$ becomes the real $x_0=c r'_{t}$, so a display writes $t'$ with no $i$ attached. The $i$ does not disappear; its square becomes the sign of the time term, $i^2=-1$, so the interval reads $-c^2t'^2+r_x^2+r_y^2+r_z^2$ with real coefficients, and the metric is still $\delta_{\mu\nu}$. Nothing is chosen a second time, and no matrix is needed: $Q_t=i c r'_t$ is the change of frame. The purpose of the frame is display: to write familiar equations in their familiar shape, with a real time and one minus on the time term. Nothing is added to the content, and the same equation is read in the notation of the textbooks.

**The interval carries one minus, and the minus is the square of the $i$.** On $\mathbb{M}_-$ the same interval reads
$$
-x_0^2+x_1^2+x_2^2+x_3^2 ,
$$
with one minus on the time term and none on the space. The minus is not a signature: it is the square of the $i$ in $Q_t=i c r'_t$, written once in the coordinate and read once here. The sign is now explicit in the coordinate, and no metric is written. The frame fixes the interval; it does not offer a choice of interval. Read on $\mathbb{M}_-$, this is the interval of the two real sectors; on $\mathbb{M}_+$ the same form is read on the informational coordinate, where the minuses sit on the space.

**The squares are the same in both frames.**
$$
\mathrm{Sc}(e_t^2)=+1,\qquad \mathrm{Sc}(\vec e_k^2)=-1,\qquad \mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu} ,
$$
with $\varepsilon=(1,-1,-1,-1)$ the plain weight. The split is in the weight, not in the frame: the same two squares hold in both, and the time direction is the one the weight leaves positive.

## The Two Frames Side by Side

Each column uses its own coordinate; the $\mathbb{B}$ column is the general frame, and the material case is named inside it.

| | $\mathbb{B}$ frame | $\mathbb{M}_-$ frame |
|---|---|---|
| coordinate | $Q_\mu\in\mathbb{C}$; on $\mathbb{M}_-$, $Q_t=i c r'_t$ | the same $Q_\mu$; on $\mathbb{M}_-$, $x_0=c r'_{t}$ and $Q_t=ix_0$ |
| interval $\sum_\mu Q_\mu^2$ | coefficients $(1,1,1,1)$; complex in general | $-c^2t'^2+r_x^2+r_y^2+r_z^2$ on $\mathbb{M}_-$ |
| metric | $\delta_{\mu\nu}=(1,1,1,1)$ | $\delta_{\mu\nu}=(1,1,1,1)$ |
| plain weight $\varepsilon$ | $(1,-1,-1,-1)$ | $(1,-1,-1,-1)$ |
| squares of the four units | $\mathrm{Sc}(e_t^2)=+1$ and $\mathrm{Sc}(\vec e_k^2)=-1$, that is $\varepsilon$ | the same, that is $\varepsilon$ |

**There is one metric and one weight, and the two frames differ in the coordinate.** The metric is $\delta_{\mu\nu}=(1,1,1,1)$ in both frames, and it is the coefficient tuple of the interval $\sum_\mu Q_\mu^2$. In the $\mathbb{M}_-$ frame the interval still has every coefficient $+1$ in the $Q$'s; written in the real coordinate it reads $-c^2t'^2+r_x^2+r_y^2+r_z^2$, and the one minus is the $i$ of $Q_t=ix_0$, which is $i^2=-1$ on the time slot. The plain weight $\varepsilon=(1,-1,-1,-1)$ is the square of the units, the same in both frames, and it is not the metric. A reader who carries the weight from one frame to the other as if it were the interval gets a sign that no algebra check will catch.

**One metric, and neither real sector adds one.** The metric is $\delta_{\mu\nu}=(1,1,1,1)$, the coefficient tuple of $\sum_\mu Q_\mu^2$, and a sector is a condition on the four coefficients, not another frame: $\mathbb{M}_-$ makes $Q_t$ imaginary, so its one minus is the square of one $i$; $\mathbb{M}_+$ makes the three space coefficients imaginary, so its three minuses are the squares of three $i$'s. Neither touches the metric. A metric that differed on one sector would be a second object, and there is none. The sign a reader sees belongs to the coordinate the square was taken in, not to the metric.

**The $i$ is never put into the metric.** The one metric, $\delta_{\mu\nu}$, has real coefficients everywhere. What changes is which coordinate carries the $i$: on the material case it is $Q_t$, in the $\mathbb{M}_-$ frame it is none. A metric with an $i$ in it is not a metric of this series.

**The substitution is the material one.** $Q_t=i c r'_t$ is made on $\mathbb{M}_-$. The informational sector has real time and imaginary space, $\tilde R_\psi=ct\,e_t+i(r'_{x}\vec e_x+r'_{y}\vec e_y+r'_{z}\vec e_z)$, and it is not obtained by the same substitution. An article that writes both sectors states which coordinate belongs to which.

## The Clifford Map

**A dictionary, not a map of the biquaternion environment.** The Clifford map is not a structure of $\mathbb{B}$. Its source is not the algebra and its target is not the algebra: the source is the four directions of one chosen frame, and the target is $M_4(\mathbb{C})$. Nothing in the multiplication of $\mathbb{B}$ produces it. It is kept here for one reason: the physics papers are written in gamma matrices, and a reader who comes from them needs the translation. The four arrays are displayed in this section and nowhere else in the article; the rest of the article writes the coordinate, the interval and the weight, and cites this section for them. It is cited, not assumed; a display that uses it declares it.

**What the framework does instead is change the frame.** Physics is studied here by choosing a coordinate frame, not by choosing matrices. In the general case the frame is $\mathbb{B}$ itself, the four coefficients $Q_\mu\in\mathbb{C}$ with the interval $\sum_\mu Q_\mu^2$. In the material sector the frame is the real frame of $\mathbb{M}_-$, reached by $Q_t=ix_0$, and that change of frame carries the physics. The map translates the change into matrices; it does not produce it.

**The map and its values.** The four directions of a frame go to the four matrices, and the map is one map for both frames:
$$
\mathsf{K}(e_\mu)=\gamma_\mu .
$$
Its values are fixed by the anticommutator,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad \varepsilon=(1,-1,-1,-1),
$$
and it is linear over the complex field in either frame. The two squares are $\gamma_0^2=+I_4$ and $\gamma_k^2=-I_4$ in both frames, and that is the weight written in the arrays. Earlier versions called the five images the gamma frame; this article names the map the Clifford map, because the object is a map and not a frame, and calls the five the gamma set. The letter $\gamma$ stays for the four images.

**The image is four-dimensional and not closed.** Four elements span four dimensions, and $M_4(\mathbb{C})$ has sixteen. A product of two distinct images is a bivector, and it leaves the image. The image is a subspace, not a subalgebra, and not a basis: the basis is the sixteen graded products, $1+4+6+4+1$. Writing the four as "the basis" hides both the count and the place each product lands.

**The weight is read from the map, and the metric is not.** The map carries one weight, $4\varepsilon_\mu\delta_{\mu\nu}=\operatorname{tr}\bigl(\mathsf{K}(e_\mu)\mathsf{K}(e_\nu)\bigr)$ in the defining representation, and that weight is the same in both frames. The metric is not a second object of the frame: there is one, $\delta_{\mu\nu}=(1,1,1,1)$, it is the coefficient tuple of the interval $\sum_\mu Q_\mu^2$, and it is the same in both frames. The two are written with two symbols because they are two objects; an article that used one for the other would be wrong in sign and would look right.

**The change of frame is the substitution, and it is written once.** On the material sector it is $Q_t=ix_0$ and $Q_k=x_k$. No matrix is written for it: a matrix here would be a second object carrying a diagonal, and the diagonal was never the content. The metric does not follow from a matrix and does not need to: it is $\delta_{\mu\nu}$ before the substitution and $\delta_{\mu\nu}$ after it. The matrices do not follow either: $\gamma_\mu$ is one array, not one array per coordinate, and the substitution leaves it alone. A display that changes frame writes $Q_t=ix_0$ once; it does not restate the matrices.

**The fifth is a product, not a direction.** The fifth is the product $i\gamma_0\gamma_1\gamma_2\gamma_3$ of the frame's four images, so it is fixed by them and is not a fifth image of the map. Being a product and not a direction, it carries no frame label: a label there would read as an argument. The glyph is $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$ with $\gamma_5^2=I_4$, and it names one operator. It differs from the volume element of the frame, which is the same product without the phase $i$, and the two are written as two glyphs and not one.

**One map, one weight.** The four matrices are the same in both frames, so an article never chooses between two maps: it chooses a coordinate, and the coordinate alone fixes the interval. There is one metric, $\delta_{\mu\nu}$. A display that writes a metric of its own has invented a second one, and no algebraic check detects it.

## The Rules

Eight rules follow.

1. **Declare the frame before the first display.** A formula that does not name its frame is read in the article's declared default, and an article declares one default only.
2. **One product, one coordinate.** A product is read in one frame's coordinate, and the coordinate fixes the interval. The metric is one, $\delta_{\mu\nu}=(1,1,1,1)$, and it is the same in both frames. The matrices carry no frame and are never relabelled.
3. **The index is low, and it labels a direction.** The index names which of the four directions is read; it is not a tensor slot, and no label is raised on the array itself: raising is done with the weight, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$. The fifth is a product and not an image of a direction, so it is written $\gamma_5$ without a label.
4. **Name the frame with its coordinate.** The coordinate frame carries its interval. A statement that names a frame names the coordinate it reads; an interval is never moved from one frame to another.
5. **The $i$ is in the coordinate or in the signs, never in the metric.** The one metric has real coefficients.
6. **$Q_t=i c r'_t$ is material.** The substitution is made on $\mathbb{M}_-$ and is not carried to $\mathbb{M}_+$ without saying so.
7. **A change of frame is a written substitution.** It has a law, $Q_t=ix_0$ in the coordinates, and the article gives it. The frame is named on the coordinate and no metric is written, because the substitution carries the interval at once. A display is read only in the frame that produced it. The substitution does not touch the matrices.
8. **The interval is a norm, not a metric.** The interval of an element is squared by multiplying it by its conjugate, $\langle\tilde X\rangle_\natural=\tilde X\tilde X^\natural$. In the $\mathbb{B}$ frame this is the plain sum $\sum_\mu Q_\mu^2$, with every coefficient $+1$. In the $\mathbb{M}_-$ frame the interval is $-c^2t'^2+r_x^2+r_y^2+r_z^2$: one minus, the square of the one $i$ of $Q_t=i c r'_t$, which is $i^2=-1$ on the time slot. The minus is the $i$ squared, not a signature, and no metric is written in either frame. The weight is not the negative of a metric: it records the square of each unit, and it is the same in both frames. The letter $\eta$ is never the metric.

**The plain weight is not a metric.** $\varepsilon=(1,-1,-1,-1)$ follows from the multiplication of the units, $\mathrm{Sc}(e_t^2)=+1$ and $\mathrm{Sc}(\vec e_k^2)=-1$. It belongs to the product, it is the same in both frames, and no frame changes it or raises it.

**The calculus is not a frame rule.** It belongs to *Operator and Calculus Conventions*. The frame supplies the coordinate and the interval, and the index stays low in both frames.

## Summary

The word *frame* here means a spacetime frame: a choice of coordinates on the biquaternion space. There are two, $\mathbb{B}$ and $\mathbb{M}_-$, and each carries its interval as part of the choice. The metric is one, $\delta_{\mu\nu}=(1,1,1,1)$, the same in both.

The $\mathbb{B}$ frame is the biquaternion space read in its own coordinate, $Q_\mu\in\mathbb{C}$: the natural complete frame, the general frame of the biquaternion universe, with interval coefficients $(1,1,1,1)$, the Euclidean form, and no reality condition. The material case is $Q_t=i c r'_t$, $Q_k=r_k$, and there the interval is the Minkowski one. The $\mathbb{M}_-$ frame is a particular case of it, kept for convenience: the material real frame, $x_0=c r'_{t}$ on $\mathbb{M}_-$, where the interval reads $-c^2t'^2+r_x^2+r_y^2+r_z^2$; the time direction is the one the weight leaves positive. On the material case the two differ by $Q_t=ix_0$.

The metric is one, and it is the tuple of the interval in the $Q$'s: $\delta_{\mu\nu}=(1,1,1,1)$ with $\sum_\mu Q_\mu^2=Q_t^2+Q_x^2+Q_y^2+Q_z^2$. In the $\mathbb{M}_-$ frame the same interval reads $-x_0^2+x_1^2+x_2^2+x_3^2$, and the one minus is the $i$ of $Q_t=ix_0$, which is $i^2=-1$ on the time slot. The plain weight $\varepsilon=(1,-1,-1,-1)$ is a different object: it belongs to the product and is the same in both frames. Naming the frame and its coordinate together is what keeps a sign from moving silently.

**The Clifford map carries the directions, not a basis.** It sends the four directions of a frame into $M_4(\mathbb{C})$; its image is four-dimensional and not closed, and its products leave it. It is a dictionary for the physics literature, not a map of $\mathbb{B}$: the framework studies physics by the change of frame, $\mathbb{B}$ in the general case and the real frame of $\mathbb{M}_-$ in the material case. The base change is the substitution $Q_t=ix_0$, written once, and the interval is read in the new coordinate after it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_\mu$ | The $\mathbb{B}$-frame coordinate, $Q_\mu\in\mathbb{C}$; material case $Q_t=i c r'_t$, $Q_k=r_k$; interval coefficients $(1,1,1,1)$ |
| $x_\mu$ | The coordinate of the $\mathbb{M}_-$ frame, on $\mathbb{M}_-$, $x_0=c r'_{t}$, $x_k=r_k$; $Q_t=ix_0$, so the interval reads $-c^2t'^2+r_x^2+r_y^2+r_z^2$ |
| $\varepsilon=(1,-1,-1,-1)$ | The plain weight, $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$; the same in both frames |
| $\langle\tilde Q\rangle_\natural=\sum_\mu Q_\mu^2$ | The quaternionic interval; coefficients $\delta_{\mu\nu}=(1,1,1,1)$ in the $Q$ coordinate (complex in general), and $-c^2t'^2+r_x^2+r_y^2+r_z^2$ read on $\mathbb{M}_-$ |
| $\delta_{\mu\nu}$ | The unit metric, the one metric of the series: diagonal, $(1,1,1,1)$ on the four $Q_\mu$, the same on the general frame and on the two real sectors |
| $\gamma_\mu$ | The four values of the Clifford map, one set for both frames, the index always low; the arrays are displayed in §*The Clifford Map* |
| $\mathsf{K}$ | The Clifford map, a dictionary from the four directions of a frame into $M_4(\mathbb{C})$, the same in both frames, not a structure of $\mathbb{B}$; its values are displayed in §*The Clifford Map* |

## Further Reading

- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the algebra, the two sectors and the coordinate $Q_t$.
- [Conventions of the Operators and the Calculus](operator-and-calculus-conventions.html), for the calculus these frames read.
- [Conventions of the Matrix Models](matrix-representations-conventions.html), for the explicit arrays and the one set of gamma matrices.
- [Conventions of the Units, the Indices and the Notation](unit-index-and-notation-conventions.html), for the two writings of the temporal slot and the index rule.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the interval, the plain weight and the other two norms.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](../articles_maths/the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the gamma matrices read as an object of their own.
