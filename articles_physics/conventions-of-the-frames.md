# __Conventions of the Frames__

## Introduction

In this article a *frame* means a spacetime frame: a choice of coordinates on the biquaternion space. There are two, the $\mathbb{B}$ frame and the $\mathbb{M}_-$ frame, and every display in the series is written in one of them. A reader who mixes the two changes a sign or a factor of $i$ and has no way to see it in the result.

This article fixes the general notion first, then the two coordinate frames. The $\mathbb{B}$ frame is the general frame of the biquaternion universe, and its metric is Euclidean. The $\mathbb{M}_-$ frame is a particular case of it on the material sector, with metric $(1,-1,-1,-1)$, kept to display familiar equations in their usual form. The article then gives the Clifford map, which translates those directions into $M_4(\mathbb{C})$ and is a dictionary rather than a structure of the algebra, and it closes with the rules that keep them apart.

Each frame is fixed with its metric. The metric is part of the frame, not a separate choice, and the plain weight belongs to the product and is the same in both frames.

The article is read after *Conventions in the Biquaternion Universe* and before *Conventions of the Matrix Models*. It uses no left or right multiplication, no cell and no explicit array.

**The order is the order of dependence, and it is also the order of risk.** The coordinate frame decides the signs of every derivative and of every square. A mistake in it propagates into every display of the article that follows.

## What a Frame Is

**A frame is a choice of coordinate, not a part of the object.** It is a rule that turns an element into four labelled components, together with a stated law for passing to another such rule. The object is what the rule leaves fixed. The metric is part of the frame, not a choice made after it: each of the two frames carries its interval. The test of a frame statement is that it names the frame and its metric; the test of an invariant statement is that it does not. A coordinate taken from one frame with the metric of the other is an object of neither, and no algebraic check detects it.

**The two coordinate frames have names.** The names are read $\mathbb{B}$ for biquaternion and $\mathbb{M}_-$ for the material sector. The $\mathbb{B}$ frame is the biquaternion space read in its own complex coordinate: the natural complete frame, with no reality condition and all four directions on the same footing. The $\mathbb{M}_-$ frame is the material real frame, named for the sector it is defined on, reached by $Q_t=ict'$ in physics and by $Q_t=iq'_t$ in mathematics. $Q_\mu$ stays the name of the complex coordinate and $x_\mu$ the name of the real one; the frame name and the coordinate name are separate. The generators carry the frame in brackets and the index low: $\gamma_\mu[\mathbb{B}]$ and $\gamma_\mu[\mathbb{M}_-]$.

**The frame and the invariant are read together.** "$\gamma_k[\mathbb{M}_-]^2=-I_4$" is a frame statement: it is true in the $\mathbb{M}_-$ frame and false for $\gamma_k[\mathbb{B}]$. "$\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2g_{\mu\nu}I_4$" is invariant in form, and the value of $g$ is what the frame supplies. Neither sentence is complete without the other.

**A change of frame is a substitution with a law.** On the material sector it is $Q_t=ix_0$ and $Q_k=x_k$ for $k=1,2,3$, with the inverse $x_0=-iQ_t$ and $x_k=Q_k$. A derivative is read only with the frame that produced it, and the substitution is written wherever a display passes from one frame to the other.

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
Every coefficient is $+1$, and the value is complex in general. The tuple is a coefficient tuple, not a real signature; a signature appears only when a sector is imposed. On $\mathbb{M}_-$, with $Q_t=ict'$, the value is $-c^2t'^2+x^2+y^2+z^2$; on $\mathbb{M}_+$, with $Q_t=ct$ and $Q_k=ix'_k$, it is $c^2t^2-x'^2-y'^2-z'^2$. The frame carries the metric $(1,1,1,1)$ as part of the choice, and on $\mathbb{M}_-$ the interval is $+g_{\mu\nu}Q_\mu Q_\nu$ with that $g$.

**The general frame, and its form is Euclidean.** The $\mathbb{B}$ frame is the frame of the biquaternion universe itself, not of one sector of it; the $\mathbb{M}_-$ frame is this one read on a sector. Its form is $\sum_\mu Q_\mu^2$, with all four coefficients $+1$. On real coefficients that is the ordinary Euclidean metric: positive definite, with no direction singled out by a sign. The coefficients are complex in general, so the form is the complexified Euclidean form; a real signature appears only when a sector is imposed. A Lorentzian signature is not a property of this frame.

**The four generators all square to $+I_4$.** In this frame the Clifford metric is the identity, $g_{\mu\nu}=\delta_{\mu\nu}$, so
$$
(\gamma_\mu[\mathbb{B}])^2=+I_4,\qquad \{\gamma_\mu[\mathbb{B}],\gamma_\nu[\mathbb{B}]\}=2\delta_{\mu\nu}I_4 .
$$
The four squares have one sign, and no generator is singled out by the sign of its square. The explicit arrays are the ones of *Conventions of the Matrix Models*.

**The material case.** On $\mathbb{M}_-$ the coefficients are
$$
Q_t=ict',\qquad Q_x=q_x,\qquad Q_y=q_y,\qquad Q_z=q_z ,
$$
with $t',q_x,q_y,q_z$ real and $c$ the local speed of light. This is the coordinate the physics corpus writes by default. It is a sector condition on the $\mathbb{B}$ frame, not the definition of the frame, and the derivative and the d'Alembertian below are written in it.

**The derivative.** The time derivative carries the $i$ of the coordinate,
$$
\frac{\partial}{\partial Q_t}=\frac{1}{ic}\frac{\partial}{\partial t'}=-\frac{i}{c}\frac{\partial}{\partial t'} .
$$

**The d'Alembertian.** With $\Delta_Q=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$,
$$
\Box=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q .
$$
It is one operator. The frame changes its reading, not its value.

## The $\mathbb{M}_-$ Frame

**The coordinate.** The $\mathbb{M}_-$ frame is the material coordinate, defined on $\mathbb{M}_-$,
$$
x_0=ct',\qquad x_1=q_x,\qquad x_2=q_y,\qquad x_3=q_z ,
$$
with $t',q_k$ real. On the material case $Q_t=ix_0$ and $Q_k=x_k$ for $k=1,2,3$: one substitution, a rotation of the time axis by $i$.

**A particular case, kept for convenience.** The $\mathbb{M}_-$ frame is the $\mathbb{B}$ frame restricted to $\mathbb{M}_-$, not a second universe and not a second algebra. It is defined only after the coefficients have been put on that sector, and its one change is the time coordinate: $Q_t=ict'$ becomes the real $x_0=ct'$, so a display writes $t'$ with no $i$ attached. The $i$ does not disappear; its square becomes the sign of the time term, $i^2=-1$, and the metric reads $(1,-1,-1,-1)$ with real coefficients. That metric is not chosen a second time: it is the Euclidean metric after the substitution, and $\Lambda^{\mathsf T}g[\mathbb{B}]\Lambda=g[\mathbb{M}_-]$ records it. The purpose of the frame is display: to write familiar equations in their familiar shape, with a real time, a real derivative and a Minkowski metric. Nothing is added to the content, and the same operator is read in the notation of the textbooks.

**The metric is $(1,-1,-1,-1)$, and the interval is its negative.** On $\mathbb{M}_-$ the same interval reads
$$
-x_0^2+x_1^2+x_2^2+x_3^2 ,
$$
with coefficients $(-1,1,1,1)$, the negative of the Clifford metric. The sign is now explicit in the coordinate. The interval is the metric up to one overall sign: $-x_0^2+x_1^2+x_2^2+x_3^2=-g_{\mu\nu}x_\mu x_\nu$ with $g=(1,-1,-1,-1)$, and the generators of the $\mathbb{M}_-$ frame realise exactly that $g$. The frame fixes the tuple; it does not offer a choice of tuple. Read on $\mathbb{M}_-$, this is the "metric of the two real sectors" of the series, not a third frame metric; on $\mathbb{M}_+$ the same form is read on the informational coordinate.

**The squares split.** In this frame
$$
(\gamma_0[\mathbb{M}_-])^2=+I_4,\qquad (\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad \{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2g_{\mu\nu}I_4 ,
$$
with $g=\mathrm{diag}(1,-1,-1,-1)$. One generator is singled out by its sign, and that generator is the time direction.

**The derivative.** The time derivative is real and carries no factor $i$:
$$
\frac{\partial}{\partial x_0}=\frac{1}{c}\frac{\partial}{\partial t'} .
$$

**The d'Alembertian.** The same operator reads
$$
\Box=\Delta-\frac{\partial^2}{\partial x_0^2},\qquad
\Delta=\frac{\partial^2}{\partial x_1^2}+\frac{\partial^2}{\partial x_2^2}+\frac{\partial^2}{\partial x_3^2}.
$$

## The Two Frames Side by Side

Each column uses its own coordinate; the $\mathbb{B}$ column is the general frame, and the material case is named inside it.

| | $\mathbb{B}$ frame | $\mathbb{M}_-$ frame |
|---|---|---|
| coordinate | $Q_\mu\in\mathbb{C}$; on $\mathbb{M}_-$, $Q_t=ict'$ | $x_0=ct'$, $x_k=q_k$ on $\mathbb{M}_-$ |
| interval $\sum_\mu Q_\mu^2$ | $(1,1,1,1)$; complex in general | $(-1,1,1,1)$ on $\mathbb{M}_-$ |
| plain weight $\varepsilon$ | $(1,-1,-1,-1)$ | $(1,-1,-1,-1)$ |
| Clifford metric $g$ | $(1,1,1,1)$ | $(1,-1,-1,-1)$ |
| squares of the four | all $+I_4$ | $(+,-,-,-)$ |
| time derivative | $\partial/\partial Q_t=-ic^{-1}\partial/\partial t'$ on $\mathbb{M}_-$ | $\partial/\partial x_0=c^{-1}\partial/\partial t'$ |
| d'Alembertian | $\partial^2/\partial Q_t^2+\Delta_Q$ on $\mathbb{M}_-$ | $\Delta-\partial^2/\partial x_0^2$ |

**Each frame makes one coincidence and breaks the other.** In the $\mathbb{B}$ frame the interval and the Clifford metric carry the same tuple, $(1,1,1,1)$; the interval's value is complex in general, and on $\mathbb{M}_-$ it is the Minkowski interval. The plain weight is $(1,-1,-1,-1)$ and does not follow either. In the $\mathbb{M}_-$ frame the plain weight and the Clifford metric coincide, both $(1,-1,-1,-1)$, and the interval has the opposite coefficients $(-1,1,1,1)$. A reader who carries "the metric" from one frame to the other carries the wrong coincidence, and the result is a sign that no algebra check will catch.

**The $i$ is never put into the metric.** The coefficients above are real in both frames. What changes is which coordinate carries the $i$: on the material case it is $Q_t$, in the $\mathbb{M}_-$ frame it is none. A metric with an $i$ in it is not a metric of this series.

**The substitution is the material one.** $Q_t=ict'$ is made on $\mathbb{M}_-$. The informational sector has real time and imaginary space, $\tilde Q_{\mathrm H}=ct\,e_t+i(x'\vec e_x+y'\vec e_y+z'\vec e_z)$, and it is not obtained by the same substitution. An article that writes both sectors states which coordinate belongs to which.

## The Clifford Map

**A dictionary, not a map of the biquaternion environment.** The Clifford map is not a structure of $\mathbb{B}$. Its source is not the algebra and its target is not the algebra: the source is the four directions of one chosen frame, and the target is $M_4(\mathbb{C})$. Nothing in the multiplication of $\mathbb{B}$ produces it. It is kept here for one reason: the physics papers are written in gamma matrices, and a reader who comes from them needs the translation. It is cited, not assumed; a display that uses it declares it.

**What the framework does instead is change the frame.** Physics is studied here by choosing a coordinate frame, not by choosing matrices. In the general case the frame is $\mathbb{B}$ itself, the four coefficients $Q_\mu\in\mathbb{C}$ with the interval $\sum_\mu Q_\mu^2$. In the material sector the frame is the real frame of $\mathbb{M}_-$, reached by $Q_t=ix_0$, and that change of frame carries the physics. The map translates the change into matrices; it does not produce it.

**The map and its values.** The two coordinate frames give four directions each, and the Clifford map sends them into $M_4(\mathbb{C})$:
$$
\mathsf{K}_{\mathbb{B}}(e_\mu)=\gamma_\mu[\mathbb{B}],\qquad
\mathsf{K}_{\mathbb{M}_-}(e_\mu)=\gamma_\mu[\mathbb{M}_-].
$$
Its values are fixed by the anticommutator in each frame,
$$
\{\gamma_\mu[\mathbb{B}],\gamma_\nu[\mathbb{B}]\}=2\delta_{\mu\nu}I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2g_{\mu\nu}I_4,\qquad g=\mathrm{diag}(1,-1,-1,-1),
$$
and it is linear over the coefficient field of its frame: complex for $\mathbb{B}$, real in the $\mathbb{M}_-$ frame. Earlier versions called the five images the gamma frame; this article names the map the Clifford map, because the object is a map and not a frame, and calls the five the gamma set. The letter $\gamma$ stays for the four images.

**The image is four-dimensional and not closed.** Four elements span four dimensions, and $M_4(\mathbb{C})$ has sixteen. A product of two distinct images is a bivector, and it leaves the image. The image is a subspace, not a subalgebra, and not a basis: the basis is the sixteen graded products, $1+4+6+4+1$. Writing the four as "the basis" hides both the count and the place each product lands.

**The metric is read from the map.** The Clifford metric is read from the anticommutator, equivalently $4g_{\mu\nu}=\operatorname{tr}\bigl(\mathsf{K}(e_\mu)\mathsf{K}(e_\nu)\bigr)$ in the defining representation. The map carries no metric of its own: the frame supplies it, and the same algebra carries both tuples.

**The change of base is one matrix.** On the material sector the change of frame is $Q_t=ix_0$; read on the generators it is
$$
\gamma_\mu[\mathbb{M}_-]=\sum_\nu\Lambda_{\mu\nu}\gamma_\nu[\mathbb{B}],\qquad
\Lambda=\Lambda_{\mathbb{B}\to\mathbb{M}_-}=\mathrm{diag}(1,-i,-i,-i).
$$
The matrix is the image of the substitution, not a second convention. The metric follows from it,
$$
\Lambda\,g[\mathbb{B}]\,\Lambda^{\mathsf T}=g[\mathbb{M}_-],\qquad g[\mathbb{B}]=\mathrm{diag}(1,1,1,1),\quad g[\mathbb{M}_-]=\mathrm{diag}(1,-1,-1,-1).
$$
The frame label is written in brackets, as it is on the generators, so no spacetime index is raised. A display that changes frame writes $\Lambda_{\mathbb{B}\to\mathbb{M}_-}$ once; it does not choose a second metric by hand.

**The fifth is a product, not a direction.** In each frame $\gamma_5$ is the product $i\gamma_0\gamma_1\gamma_2\gamma_3$ of that frame's four images, so it is fixed by them and is not a fifth image of the map. In the $\mathbb{B}$ frame the fifth is $-i$ times the fifth of the $\mathbb{M}_-$ frame, so its square is $-I_4$ there and $+I_4$ in the $\mathbb{M}_-$ frame, while the volume element $\Pi=\gamma_0\gamma_1\gamma_2\gamma_3$ of that frame has the opposite sign in each: $+I_4$ in the $\mathbb{B}$ frame and $-I_4$ in the $\mathbb{M}_-$ frame.

**Which map is displayed.** The physics articles display $\mathsf{K}_{\mathbb{M}_-}$ by default, because the derivative there is real. An article that displays $\mathsf{K}_{\mathbb{B}}$ says so at the display. The two are never mixed in one contraction.

## The Rules

Seven rules follow.

1. **Declare the frame before the first display.** A formula that does not name its frame is read in the article's declared default, and an article declares one default only.
2. **One contraction, one frame.** $\gamma_\mu[\mathbb{B}]\partial/\partial Q_\mu$ or $i\gamma_\mu[\mathbb{M}_-]\partial/\partial x_\mu$; never $i\gamma_\mu[\mathbb{M}_-]\partial/\partial Q_\mu$.
3. **The gamma index is low, and the frame is in brackets.** $\gamma_\mu[\mathbb{B}]$, $\gamma_\mu[\mathbb{M}_-]$. The index labels which direction is mapped; it is not a tensor slot. No label is raised, and no generator is written without its frame outside a declared default.
4. **Name the metric with its frame.** The coordinate frame carries its interval. A statement that names a frame names the metric it carries; a metric is never moved from one frame to another.
5. **The $i$ is in the coordinate or in the signs, never in the metric.** The coefficients of both frame metrics are real.
6. **$Q_t=ict'$ is material.** The substitution is made on $\mathbb{M}_-$ and is not carried to $\mathbb{M}_+$ without saying so.
7. **A change of frame is a written substitution.** It has a law, $Q_t=ix_0$ in the coordinates or $\Lambda_{\mathbb{B}\to\mathbb{M}_-}$ on the generators, and the article gives it. A derivative is read only with the frame that produced it.

**The plain weight is not a frame metric.** $\varepsilon=(1,-1,-1,-1)$ follows from the multiplication of the units, $\mathrm{Sc}(e_t^2)=+1$ and $\mathrm{Sc}(\vec e_k^2)=-1$. It belongs to the product, it is the same in both frames, and no frame changes it or raises it.

**A contraction uses the plain weight.** The contraction of a derivative with a field is the scalar part of the product, $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle=\sum_\mu\varepsilon_\mu\,\partial_\mu Q_{\mathrm f\mu}$. The indices stay low and the weight is in the sum. A contraction written with one raised and one lowered index imports a metric tensor the series does not use, and it hides which of the two frame metrics is meant.

## The Same Operator in Both Frames

**Both contractions square to the d'Alembertian.** Take the material case. In the $\mathbb{B}$ frame,
$$
\Bigl(\gamma_\mu[\mathbb{B}]\frac{\partial}{\partial Q_\mu}\Bigr)^2
=\sum_\mu\frac{\partial^2}{\partial Q_\mu^2}\,I_4=\Box I_4 ,
$$
because the cross terms cancel by anticommutation and every square is $+I_4$. In the $\mathbb{M}_-$ frame,
$$
\Bigl(i\gamma_\mu[\mathbb{M}_-]\frac{\partial}{\partial x_\mu}\Bigr)^2
=-\Bigl(\frac{\partial^2}{\partial x_0^2}-\Delta\Bigr)I_4=\Box I_4 ,
$$
because the squares are $(+,-,-,-)$ and the $i$ in front supplies the overall minus.

**The mixed form is neither.** The contraction $i\gamma_\mu[\mathbb{M}_-]\partial/\partial Q_\mu$ squares to
$$
\Bigl(\Delta+\frac{1}{c^2}\frac{\partial^2}{\partial {t'}^{2}}\Bigr)I_4 ,
$$
which differs from $\Box$ by the sign of the time term. It is not a third frame and it is not written.

**The check is a square, not an entry.** A reader can test a frame statement without any array: square the operator and compare with $\Box$. The coordinate frame and the sign of the metric are tested at once.

## Summary

The word *frame* here means a spacetime frame: a choice of coordinates on the biquaternion space. There are two, $\mathbb{B}$ and $\mathbb{M}_-$, and each carries its metric as part of the choice.

The $\mathbb{B}$ frame is the biquaternion space read in its own coordinate, $Q_\mu\in\mathbb{C}$: the natural complete frame, the general frame of the biquaternion universe, with interval coefficients $(1,1,1,1)$, the Euclidean form, every generator squaring to $+I_4$, and no reality condition. The material case is $Q_t=ict'$, $Q_k=q_k$, and there the interval is the Minkowski one. The $\mathbb{M}_-$ frame is a particular case of it, kept for convenience: the material real frame, $x_0=ct'$ on $\mathbb{M}_-$ with metric $(1,-1,-1,-1)$; the time generator is the one with the positive square. On the material case the two differ by $Q_t=ix_0$, and both contractions square to the same $\Box$.

The metric is carried by the frame. The $\mathbb{B}$ frame carries $(1,1,1,1)$ and its interval is the same tuple, $Q_t^2+Q_x^2+Q_y^2+Q_z^2$. The $\mathbb{M}_-$ frame carries $(1,-1,-1,-1)$ and its interval is the negative, $(-1,1,1,1)$; the two differ by the one sign of $Q_t=ix_0$. The plain weight $\varepsilon=(1,-1,-1,-1)$ is the exception: it belongs to the product and is the same in both frames. Naming the frame and its metric together is what keeps a sign from moving silently.

**The Clifford map carries the directions, not a basis.** It sends the four directions of a frame into $M_4(\mathbb{C})$; its image is four-dimensional and not closed, and its products leave it. It is a dictionary for the physics literature, not a map of $\mathbb{B}$: the framework studies physics by the change of frame, $\mathbb{B}$ in the general case and the real frame of $\mathbb{M}_-$ in the material case. The base change is the one matrix $\Lambda_{\mathbb{B}\to\mathbb{M}_-}=\mathrm{diag}(1,-i,-i,-i)$, the image of $Q_t=ix_0$ on the generators, and the metric transforms with it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_\mu$ | The $\mathbb{B}$-frame coordinate, $Q_\mu\in\mathbb{C}$; material case $Q_t=ict'$, $Q_k=q_k$; interval coefficients $(1,1,1,1)$ |
| $x_\mu$ | The coordinate of the $\mathbb{M}_-$ frame, on $\mathbb{M}_-$, $x_0=ct'$, $x_k=q_k$; metric $(1,-1,-1,-1)$ |
| $\varepsilon=(1,-1,-1,-1)$ | The plain weight, $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$; the same in both frames |
| $\langle\tilde Q\rangle_\natural=\sum_\mu Q_\mu^2$ | The quaternionic interval; coefficients $(1,1,1,1)$ in the $\mathbb{B}$ frame (complex in general), $(-1,1,1,1)$ in the $\mathbb{M}_-$ frame |
| $g_{\mu\nu}$ | The Clifford metric of the frame; $(1,1,1,1)$ in the $\mathbb{B}$ frame, $(1,-1,-1,-1)$ in the $\mathbb{M}_-$ frame |
| $\gamma_\mu[\mathbb{B}]$, $\gamma_\mu[\mathbb{M}_-]$ | The values of the Clifford map in each frame, $\gamma_k[\mathbb{B}]=i\gamma_k[\mathbb{M}_-]$; the index is always low |
| $\mathsf{K}_{\mathbb{B}}$, $\mathsf{K}_{\mathbb{M}_-}$ | The Clifford map, $\mathsf{K}_{\mathbb{B}}(e_\mu)=\gamma_\mu[\mathbb{B}]$ and $\mathsf{K}_{\mathbb{M}_-}(e_\mu)=\gamma_\mu[\mathbb{M}_-]$; a dictionary from the four directions into $M_4(\mathbb{C})$, not a structure of $\mathbb{B}$ |
| $\Lambda_{\mathbb{B}\to\mathbb{M}_-}$ | $\mathrm{diag}(1,-i,-i,-i)$, the base change $\gamma_\mu[\mathbb{M}_-]=\sum_\nu\Lambda_{\mu\nu}\gamma_\nu[\mathbb{B}]$ |
| $\Box$ | $\partial^2/\partial Q_t^2+\Delta_Q=\Delta-\partial^2/\partial x_0^2$ |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the algebra, the two sectors and the coordinate $Q_t$.
- [Conventions of the Operators and the Calculus](conventions-of-the-operators-and-the-calculus.html), for the gradient and the d'Alembertian these frames read.
- [Conventions of the Matrix Models](conventions-of-the-matrix-models.html), for the explicit arrays and the gamma matrices in each frame.
- [Conventions of the Units, the Indices and the Notation](conventions-of-the-units-the-indices-and-the-notation.html), for the two writings of the temporal slot and the index rule.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the interval, the plain weight and the other two norms.
- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](../articles_maths/the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the gamma matrices read as an object of their own.
