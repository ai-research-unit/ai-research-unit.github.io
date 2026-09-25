
# __Real Integration__

## Introduction

This is the seventh article of the Real Numbers system in Part V, and it occupies the **integration slot** of that system. The system is the ordered field $\mathbb{R}$ of *The Real Numbers*, and the object of study is the integral of a function of one real variable over an interval: the Riemann integral of the bounded functions on a compact interval, the fundamental theorem of calculus in both directions, the techniques of integration, the improper integrals over unbounded domains, and the Riemann–Stieltjes integral together with its role as the general form of a positive linear functional.

The differential and sequential theory of the line is from *Real Analysis*, and the parts of the present article that concern the elementary theory of the Riemann integral are developed there; the purpose of this article is to isolate the integral as the *slot* of the system $\mathbb{R}$, that is, as the pairing of the line with its dual of functions, and to carry the theory to the point — the Riemann–Stieltjes integral, its integration by parts, the Riesz representation theorem and the comparison with Lebesgue integration — at which the integral of the line becomes a structure in its own right. The measure-theoretic integral on a general measure space is from *Measure Theory and Integration*, and the comparison is drawn where it matters; the special functions of the line, which are the next slot of the system, are not used.

Throughout, $[a,b]$ is a compact interval with $a < b$, a **partition** is a finite set $P = \{a = x_0 < x_1 < \cdots < x_n = b\}$, and for a bounded function $f$ on $[a,b]$ the **upper and lower sums** are

$$
U(f,P) = \sum_{i=1}^{n} \sup_{[x_{i-1}, x_i]} f \cdot (x_i - x_{i-1}), \qquad L(f,P) = \sum_{i=1}^{n} \inf_{[x_{i-1}, x_i]} f \cdot (x_i - x_{i-1}) .
$$

The integrand is a bounded real function unless stated, the integral is written $\int_a^b f$ or $\int_a^b f(x)\,dx$, the **mesh** of $P$ is $\lVert P\rVert = \max_i (x_i - x_{i-1})$, and $\operatorname{BV}[a,b]$ is the space of functions of bounded variation on $[a,b]$. The integral of a function vanishing outside $[a,b]$ over all of $\mathbb{R}$ is written with the corresponding limits.

## The Riemann Integral

### Partitions and Darboux Sums

**Definition.** For a bounded $f : [a,b] \to \mathbb{R}$ the **upper integral** and the **lower integral** are

$$
\overline{\int_a^b} f = \inf_P U(f,P), \qquad \underline{\int_a^b} f = \sup_P L(f,P),
$$

the infimum and supremum over all partitions $P$ of $[a,b]$. The function $f$ is **Riemann integrable** if the two agree, and the common value is the integral $\int_a^b f$.

**Theorem.** For every bounded $f$ and every pair of partitions $P, Q$ one has $L(f,P) \leq U(f,Q)$; consequently $\underline{\int} f \leq \overline{\int} f$, and $f$ is integrable if and only if for every $\varepsilon > 0$ there is a partition $P$ with

$$
U(f,P) - L(f,P) < \varepsilon .
$$

**Proof.** Refining a partition increases the lower sum and decreases the upper sum, so it suffices to compare $P$ and $Q$ by passing to their common refinement $P \cup Q$, for which $L(f,P) \leq L(f, P\cup Q) \leq U(f, P\cup Q) \leq U(f,Q)$. The criterion follows because the infimum of the upper sums and the supremum of the lower sums then coincide exactly when their gap can be made smaller than every $\varepsilon$. $\square$

**Definition.** The **oscillation** of $f$ on a set $E$ is $\operatorname{osc}_E f = \sup_E f - \inf_E f$; the **modulus of the partition** of $f$ on $P$ is the sum $\sum_i \operatorname{osc}_{[x_{i-1},x_i]} f \cdot (x_i - x_{i-1}) = U(f,P) - L(f,P)$.

**Theorem (Riemann sums).** A bounded $f$ is integrable with integral $I$ if and only if for every $\varepsilon > 0$ there is $\delta > 0$ such that

$$
\left\lvert \sum_{i=1}^{n} f(\xi_i)(x_i - x_{i-1}) - I \right\rvert < \varepsilon
$$

for every partition $P$ with $\lVert P\rVert < \delta$ and every choice of tags $\xi_i \in [x_{i-1}, x_i]$.

**Proof.** A tagged Riemann sum lies between the lower and upper sums of $P$, so the criterion for integrability implies the convergence of the sums. Conversely, if the sums converge to $I$ uniformly in the tags, then the largest and smallest tagged sums for a partition of small mesh both lie within $\varepsilon$ of $I$, so $U(f,P) - L(f,P) < 2\varepsilon$ and $f$ is integrable with integral $I$. $\square$

**Theorem.** Every continuous function on $[a,b]$ is Riemann integrable, and every monotone function on $[a,b]$ is Riemann integrable.

**Proof.** A continuous function on a compact interval is uniformly continuous, so on a partition of sufficiently small mesh every oscillation is less than $\varepsilon$, giving $U - L \leq \varepsilon(b-a)$. A monotone function has total oscillation $f(b) - f(a)$ distributed over the partition, so the oscillation sum is at most $(f(b)-f(a))\lVert P\rVert$. $\square$

### Lebesgue's Criterion

**Theorem (Lebesgue).** A bounded function $f : [a,b] \to \mathbb{R}$ is Riemann integrable if and only if the set $D_f$ of its points of discontinuity has Lebesgue measure zero.

**Proof.** If $f$ is integrable, then for each $k$ the set of points where the oscillation exceeds $1/k$ can be covered by finitely many intervals of arbitrarily small total length, so each such set has measure zero, and $D_f$ is a countable union of them. Conversely, if $D_f$ has measure zero and $\lvert f\rvert \leq M$, cover $D_f$ by finitely many intervals of total length $\varepsilon/(4M)$ and partition the complement, where $f$ is uniformly continuous, finely enough that the oscillation is small; the partition so obtained satisfies $U - L < \varepsilon$. The criterion is the classical one of Lebesgue and the argument is in the references. $\square$

**Corollary.** A bounded function is Riemann integrable exactly when it is continuous almost everywhere, so the integrable functions include the continuous, the monotone and the bounded functions with countably many discontinuities, and exclude the indicator of a fat Cantor set. The set of Riemann integrable functions on $[a,b]$ is a vector space closed under products and under the lattice operations, and it contains the continuous functions as a dense subspace in the supremum norm.

**Proof.** The almost-everywhere continuity follows from the criterion and the subadditivity of measure. The algebraic closure is checked directly from the definition by the oscillation estimates $\operatorname{osc}(f+g) \leq \operatorname{osc} f + \operatorname{osc} g$ and $\operatorname{osc}(fg) \leq \lVert f\rVert_\infty \operatorname{osc} g + \lVert g\rVert_\infty \operatorname{osc} f$. $\square$

## Properties of the Integral

### Linearity and Order

**Theorem.** Let $f, g$ be Riemann integrable on $[a,b]$ and let $\lambda \in \mathbb{R}$. Then

$$
\int_a^b (f + g) = \int_a^b f + \int_a^b g, \qquad \int_a^b \lambda f = \lambda \int_a^b f, \qquad f \leq g \implies \int_a^b f \leq \int_a^b g .
$$

Moreover the integral is additive over subintervals: for $a \leq c \leq b$,

$$
\int_a^b f = \int_a^c f + \int_c^b f ,
$$

and $\lvert \int_a^b f\rvert \leq \int_a^b \lvert f\rvert \leq \lVert f\rVert_\infty (b-a)$.

**Proof.** The upper and lower sums are additive and homogeneous in the integrand for a fixed partition, and the monotonicity is immediate from $\sup f \leq \sup g$ and $\inf f \leq \inf g$ pointwise; the additivity over subintervals follows by adjoining the point $c$ to a partition, and the triangle inequality by applying monotonicity to $\pm f \leq \lvert f\rvert$. $\square$

**Definition.** The function $x \mapsto \int_a^x f$ is the **indefinite integral** of $f$ from $a$, and the **mean value** of $f$ on $[a,b]$ is $\frac{1}{b-a}\int_a^b f$.

**Theorem (mean value theorems for the integral).** If $f$ is continuous on $[a,b]$ then its mean value is attained: there is $\xi \in [a,b]$ with

$$
\int_a^b f = f(\xi)(b-a),
$$

and if in addition $f$ is differentiable on $(a,b)$ then $\xi$ may be taken in the interior; more generally, if $g \geq 0$ is integrable and $f$ continuous, there is $\xi$ with $\int_a^b fg = f(\xi)\int_a^b g$.

**Proof.** The first statement is the extreme value theorem applied to $f$ together with the intermediate value theorem: the mean value lies between the minimum and the maximum of $f$. The second is the same after the observation that the mean is strictly between the endpoint values under differentiability; the weighted form follows by the same argument with the weights $g$. $\square$

### The Integral as a Functional

**Theorem.** The map $f \mapsto \int_a^b f$ is a positive linear functional on the space of Riemann integrable functions, and it is bounded with respect to the supremum norm: $\lvert\int_a^b f\rvert \leq (b-a)\lVert f\rVert_\infty$. It is translation-invariant in the sense that $\int_a^b f(x + t)\,dx = \int_{a+t}^{b+t} f(x)\,dx$, and it is the unique positive linear functional on the continuous functions, up to a positive scalar, that is invariant under all translations of the line.

**Proof.** Linearity is the previous theorem; the bound is the triangle inequality; translation invariance is the change of variables $x \mapsto x+t$, which is an isometry of the line. Uniqueness up to scale is the one-dimensional case of the uniqueness of Haar measure on a locally compact group, as in *Topological Groups* and *Measure Theory and Integration*. $\square$

**Remark.** The uniqueness is the algebraic statement of the geometric fact that the integral is the length: the only positive linear functionals invariant under the isometries of the line are the scalar multiples of the integral, and the scalar is fixed by declaring the integral of the indicator of $[0,1]$ to be $1$. This is the integration slot's contribution to the geometry of the system: the length of *Real Line Geometry and Isometries* is the same object as the integral of the indicator function of an interval.

## The Fundamental Theorem of Calculus

### Both Directions

**Theorem (fundamental theorem, first form).** Let $f$ be Riemann integrable on $[a,b]$ and let $F(x) = \int_a^x f$. Then $F$ is continuous on $[a,b]$ and Lipschitz with constant $\lVert f\rVert_\infty$; and if $f$ is continuous at $x_0 \in (a,b)$ then $F$ is differentiable at $x_0$ with $F'(x_0) = f(x_0)$. Consequently if $f$ is continuous on $[a,b]$ then $F$ is differentiable with $F' = f$.

**Proof.** The estimate $\lvert F(x) - F(y)\rvert \leq \lVert f\rVert_\infty \lvert x-y\rvert$ gives the Lipschitz property. If $f$ is continuous at $x_0$, then for $h \neq 0$,

$$
\frac{F(x_0+h) - F(x_0)}{h} - f(x_0) = \frac{1}{h}\int_{x_0}^{x_0+h} (f(t) - f(x_0))\,dt,
$$

and the absolute value is at most $\sup_{\lvert t-x_0\rvert \leq \lvert h\rvert}\lvert f(t) - f(x_0)\rvert$, which tends to $0$ with $h$. $\square$

**Theorem (fundamental theorem, second form).** If $F$ is differentiable on $[a,b]$ with $F'$ Riemann integrable, then

$$
\int_a^b F' = F(b) - F(a) .
$$

Consequently every Riemann integrable function with a primitive satisfies the evaluation formula, and primitives differ by constants.

**Proof.** For a partition $P$, the mean value theorem applied on each subinterval gives $\xi_i$ with $F(x_i) - F(x_{i-1}) = F'(\xi_i)(x_i - x_{i-1})$, and summing gives the tagged Riemann sum $F(b)-F(a)$; as the mesh tends to $0$ the sums converge to $\int_a^b F'$ by integrability. Hence $F(b) - F(a) = \int_a^b F'$, and two primitives of the same function have zero derivative, hence differ by a constant. $\square$

### Techniques

**Theorem (integration by parts).** If $u, v$ are differentiable on $[a,b]$ with $u', v'$ Riemann integrable, then

$$
\int_a^b u\,v' = u(b)v(b) - u(a)v(a) - \int_a^b u'\, v .
$$

**Proof.** The product rule gives $(uv)' = u'v + uv'$, and both sides are Riemann integrable; the second fundamental theorem applied to $uv$ gives the identity. $\square$

**Theorem (substitution).** Let $\varphi : [\alpha,\beta] \to [a,b]$ be continuously differentiable and increasing with $\varphi(\alpha) = a$, $\varphi(\beta) = b$, and let $f$ be continuous on $[a,b]$. Then

$$
\int_a^b f(x)\,dx = \int_\alpha^\beta f(\varphi(t))\,\varphi'(t)\,dt .
$$

**Proof.** Both sides are differentiable functions of the upper limit with the same derivative, by the chain rule and the first fundamental theorem; they agree at the lower limit, hence everywhere. $\square$

## Improper Integrals

### Convergence and Its Criteria

**Definition.** For $f$ integrable on every $[a,c]$ with $c > a$, the **improper integral** $\int_a^\infty f$ is the limit $\lim_{c\to\infty}\int_a^c f$ when it exists, and $f$ is then **improperly integrable**; if $\int_a^\infty \lvert f\rvert$ converges, the integral **converges absolutely**, and otherwise it **converges conditionally**. The same definitions apply to unbounded integrands on a bounded interval.

**Theorem (comparison and Dirichlet tests).** If $0 \leq f \leq g$ and $\int_a^\infty g$ converges, then $\int_a^\infty f$ converges. If $F(c) = \int_a^c f$ is bounded and $g$ decreases to $0$, then $\int_a^\infty f g$ converges; in particular

$$
\int_1^\infty \frac{dx}{x^p} \text{ converges } \iff p > 1, \qquad \int_0^\infty \frac{\sin x}{x}\,dx = \frac{\pi}{2} \text{ converges conditionally.}
$$

**Proof.** The comparison test is the monotone convergence of the function $c \mapsto \int_a^c f$ bounded above. The Dirichlet test is the second mean value theorem applied to $F$ and $g$, which shows that the tails of $\int fg$ are bounded by $2\lVert F\rVert_\infty\, g(N)$. The $p$-integral is computed by the second fundamental theorem, giving $\frac{1}{p-1}$ for $p>1$ and divergence for $p \leq 1$; the Dirichlet integral is evaluated by the standard contour or parameter-differentiation argument and converges conditionally because $\int_1^\infty \lvert \sin x\rvert/x\,dx$ diverges. $\square$

**Definition.** For a function with a singularity at an interior point, the **Cauchy principal value** is

$$
\mathrm{p.v.}\int_{-\infty}^{\infty} f = \lim_{R\to\infty}\int_{-R}^{R} f ,
$$

which may exist when the improper integral does not; the principal value of $\int_{-\infty}^\infty x\,dx$ is $0$, while the improper integral does not exist.

## The Riemann–Stieltjes Integral

### Definition and Integration by Parts

**Definition.** Let $f, g : [a,b] \to \mathbb{R}$ and let $P$ be a partition with tags $\xi_i$. The **Riemann–Stieltjes sum** is

$$
S(f,g,P) = \sum_{i=1}^{n} f(\xi_i)\,(g(x_i) - g(x_{i-1})) ,
$$

and $f$ is **Riemann–Stieltjes integrable** with respect to $g$ with integral $\int_a^b f\,dg$ if the sums converge as the mesh tends to $0$, uniformly in the tags.

**Theorem (existence).** If $f$ is continuous and $g$ is of bounded variation on $[a,b]$, then $\int_a^b f\,dg$ exists. If $g$ is continuously differentiable, then $\int_a^b f\,dg = \int_a^b f g'\,dx$, and if $g$ is the indicator of $[c,b]$ with $a < c < b$, the integral is $f(c)$.

**Proof.** A function of bounded variation is the difference of two increasing functions, and for an increasing integrator the sums for a refinement are between the lower and upper Stieltjes sums, which differ by $\operatorname{osc} f \cdot (g(b)-g(a))$ and hence tend to $0$ by the uniform continuity of $f$. The smooth case follows by the mean value theorem and the reduction to Riemann sums; the jump case is immediate from the definition. $\square$

**Theorem (integration by parts).** If $\int_a^b f\,dg$ exists then $\int_a^b g\,df$ exists and

$$
\int_a^b f\,dg = f(b)g(b) - f(a)g(a) - \int_a^b g\,df .
$$

**Proof.** Both sides are obtained by the Abel summation identity applied to a partition: the identity rearranges a Stieltjes sum for $f$ against $g$ into a boundary term minus a Stieltjes sum for $g$ against $f$, and the existence of one integral therefore gives the existence of the other and the displayed formula. $\square$

**Theorem (Riesz representation).** Every bounded linear functional $\Lambda$ on the space $C[a,b]$ of continuous functions with the supremum norm is of the form

$$
\Lambda(f) = \int_a^b f\,dg
$$

for a function $g$ of bounded variation, unique if normalised by $g(a) = 0$ and right-continuity in the interior. The functional is positive if and only if $g$ is increasing, and its norm is the total variation of $g$.

**Proof.** The theorem is Riesz's. A bounded linear functional on $C[a,b]$ is uniformly continuous for the supremum norm, so it extends uniquely to the uniform closure of the step functions, which is the space of regulated functions; the representing function is then $g(x) = \tilde\Lambda(\mathbf{1}_{(a,x]})$, which has bounded variation with $g(a) = 0$ and is right-continuous on $(a,b)$, and the Stieltjes integral of $f$ against it recovers $\Lambda(f)$. Positivity of $\Lambda$ makes $g$ increasing, and the norm of $\Lambda$ is the total variation of $g$ by the definition of the Stieltjes integral. The proof is in *Measure Theory and Integration*. $\square$

**Remark.** The Riesz representation is the precise form in which the integral of the line is its own dual: the continuous functions on a compact interval have as their dual the signed measures, identified with the functions of bounded variation, and the pairing is the Stieltjes integral. This is the integration slot's structural theorem, and it is the one-dimensional case of the duality between $C_0(X)$ and the space of Radon measures.

## Comparison with the Lebesgue Integral

**Theorem.** Every Riemann integrable function on $[a,b]$ is Lebesgue integrable, and the two integrals agree. The class of Lebesgue integrable functions is strictly larger: for example the indicator of a fat Cantor set is Lebesgue integrable and not Riemann integrable, and the Dirichlet function $\mathbf{1}_{\mathbb{Q}}$ is Lebesgue integrable with integral $0$ and not Riemann integrable.

**Proof.** A Riemann integrable function is bounded and continuous almost everywhere by Lebesgue's criterion; a bounded function that is measurable and almost everywhere continuous is Lebesgue integrable, and the equality of the integrals follows by comparing the Riemann sums with the Lebesgue integral over the finitely many intervals of a partition. The stated examples are bounded, measurable and discontinuous on a set of positive measure (Cantor set) or everywhere (Dirichlet function), hence not Riemann integrable. $\square$

**Theorem (dominated and monotone convergence).** The Lebesgue integral admits the monotone convergence theorem and the dominated convergence theorem, which the Riemann integral does not admit in the same generality; for a uniformly convergent sequence of Riemann integrable functions the limit is Riemann integrable and the integrals converge, and for a bounded pointwise convergent sequence the limit need not be Riemann integrable.

**Proof.** The convergence theorems are the content of *Measure Theory and Integration*; the uniform convergence statement for the Riemann integral is the standard interchange of limit and integral under the supremum norm, and the failure of the bounded pointwise statement is witnessed by an enumeration of the rationals and the indicator functions of its finite initial segments. $\square$

**Remark.** On a compact interval the Riemann integral is sufficient for all the functions that occur in the special functions and the harmonic analysis of the system $\mathbb{R}$: those functions are continuous, piecewise continuous, or regulated, and the improper integrals that arise converge absolutely or conditionally in the classical sense. The Lebesgue integral is needed where the generality is genuinely used, namely in the measure theory of Part III, in the interchange theorems, and in the extension of the theory to the $L^p$ spaces; the present article therefore stops at the comparison, and the measure-theoretic construction is the subject of *Measure Theory and Integration*.

## Summary

The Riemann integral of a bounded function on $[a,b]$ is defined by the upper and lower Darboux sums, whose infimum and supremum agree for an integrable function; integrability is equivalent to the existence of a partition with $U - L < \varepsilon$ and to the convergence of the tagged Riemann sums, and by Lebesgue's criterion the bounded functions that are Riemann integrable are exactly those that are continuous almost everywhere. Continuous functions, monotone functions and bounded functions with few discontinuities are integrable, the integrable functions form a vector space closed under products and lattice operations, and the integral is linear, positive, additive over subintervals and bounded by $\lVert f\rVert_\infty(b-a)$.

The fundamental theorem of calculus holds in both directions: the indefinite integral of an integrable function is Lipschitz, its derivative is the integrand at every continuity point, and if a differentiable $F$ has Riemann integrable derivative then $\int_a^b F' = F(b) - F(a)$; the parts and substitution formulas follow. Improper integrals over unbounded intervals converge under comparison with the $p$-integrals and under the Dirichlet test, with the Dirichlet integral $\int_0^\infty \sin x/x\,dx = \pi/2$ as the standard conditionally convergent example, and the Cauchy principal value is defined for the symmetric truncations. The Riemann–Stieltjes integral with respect to a function of bounded variation exists for continuous integrands, admits integration by parts, and gives the Riesz representation of the bounded linear functionals on $C[a,b]$ as the Stieltjes integrals against normalised functions of bounded variation. Every Riemann integrable function is Lebesgue integrable with the same integral, the Lebesgue class is strictly larger, and the Lebesgue integral supplies the convergence theorems that the Riemann integral lacks; but on the line and for the functions the corpus uses, the Riemann integral suffices. The integration slot of the system $\mathbb{R}$ is thus complete: it is the pairing of the line with its dual, the source of the length of the geometry and of the duality of the continuous functions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $[a,b]$ | Compact interval |
| $P$, $\lVert P\rVert$ | Partition, and its mesh |
| $U(f,P)$, $L(f,P)$ | Upper and lower Darboux sums |
| $\overline{\int}$, $\underline{\int}$ | Upper and lower integrals |
| $\int_a^b f$, $\int_a^b f\,dg$ | Riemann and Riemann–Stieltjes integrals |
| $\operatorname{osc}_E f$ | Oscillation of $f$ on $E$ |
| $F(x) = \int_a^x f$ | Indefinite integral |
| $D_f$ | Set of discontinuities of $f$ |
| $\operatorname{BV}[a,b]$ | Functions of bounded variation |
| $\mathrm{p.v.}$ | Cauchy principal value |
| $\mathbf{1}_{A}$ | Indicator (characteristic function) of $A$ |
| $C[a,b]$, $\lVert\cdot\rVert_\infty$ | Continuous functions, supremum norm |

## Further Reading

- Walter Rudin, *Principles of Mathematical Analysis* (McGraw–Hill, 3rd ed. 1976), for the Riemann integral, the fundamental theorem and the improper integrals.
- Tom M. Apostol, *Mathematical Analysis* (Addison-Wesley, 2nd ed. 1974), for the Riemann–Stieltjes integral, its properties and the Riesz representation theorem.
- Henri Lebesgue, *Leçons sur l'intégration et la recherche des fonctions primitives* (Gauthier-Villars, 1904), for the criterion of Riemann integrability in terms of the set of discontinuities.
- Frigyes Riesz and Béla Sz.-Nagy, *Functional Analysis* (Dover, 1990), for the Riesz representation theorem and the duality of $C[a,b]$ with the functions of bounded variation.
- Elias M. Stein and Rami Shakarchi, *Real Analysis: Measure Theory, Integration, and Hilbert Spaces* (Princeton University Press, 2005), for the comparison of the Riemann and Lebesgue integrals and the convergence theorems.
- Russell A. Gordon, *The Integrals of Lebesgue, Denjoy, Henstock–Kurzweil, and McShane* (American Mathematical Society, 1994), for the hierarchy of integrals on the line and the precise extent of the Riemann theory.
