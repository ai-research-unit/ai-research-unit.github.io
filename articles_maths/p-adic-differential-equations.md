
# __p-adic Differential Equations__

## Introduction

A differential equation over a $p$-adic field is a differential equation whose coefficients are convergent power series and whose solutions are required to converge in the $p$-adic absolute value. The formal theory is the same as over any field of characteristic zero: the equation $y' = Ay$ has a unique formal solution with prescribed initial value. What is different, and what makes the subject a subject, is convergence. The solution of $y' = y$ is the exponential, which over $\mathbb{Q}_p$ converges only on the disc of radius $\lvert p \rvert^{1/(p-1)}$ although the coefficient $A = 1$ is a polynomial; a solution that is formal and analytic over $\mathbb{C}$ may therefore fail to converge over $\mathbb{Q}_p$, and the central problem of the theory is to decide, from the coefficients, whether a formal solution converges and on which disc. The tool that answers the question at a boundary point is the **Robba ring**, the ring of functions analytic on an annulus $r \leq \lvert x \rvert < 1$ for some $r > 0$, together with the structure theory of differential modules over it.

This article presents the theory from the beginning. It defines the differential rings of convergent power series, sets up differential modules and the equation $y' = Ay$, proves formal existence and uniqueness, exhibits the failure of convergence by the exponential, and states Dwork's lemma, the criterion that converts a divisibility condition on a power series into convergence on the open unit disc. It then defines the Robba ring, records Lazard's theorem that it is a Bézout doma, states the Dwork–Robba slope decomposition of a differential module over it, treats the Fuchsian case $xy' = By$ and the notion of solvability at a boundary point, and closes with the Christol–Dwork criterion, which characterises the algebraic power series among those that converge on the open unit disc. The theory is the analytic machinery behind the rationality of the zeta function of a variety over a finite field, and it is one of the routes to the arithmetic .

The prerequisites are *Analytic Functions and Power Series* and *Non-Archimedean Analysis* for convergent series, the radius of convergence, the exponential and the maximum principle; *p-adic Analysis* for the unit disc, Mahler's theorem and the Newton polygon, for the affinoid theory and the geometric language of annuli; *Linear Algebra* and *Modules* for the finite free modules and their bases; and *Galois Theory* for the finite extensions used in the ramified statements. The differential calculus used is the formal one of a K-derivation, which needs no order and is therefore available in the non-Archimedean setting; the corresponding Archimedean theory is that of differential equations in the complex doma, treated in the synthetic part of the corpus.

Throughout, $K$ is a complete non-Archimedean field of characteristic $0$ with absolute value $\lvert \cdot \rvert$, valuation $v$, valuation ring $\mathcal{O}$, maximal ideal $\mathfrak{m}$ and residue field $k$ of characteristic $p$; the normalisation $\lvert p \rvert = p^{-1}$ is used when the value group is discrete. The disc and the radius $\rho_{\exp} = \lvert p \rvert^{1/(p-1)}$ are those of *Analytic Functions and Power Series*. The derivation $d/dx$ is written $\partial$ or a prime, the ring of power series converging on the open unit disc is $K\{x\}$, the ring of those converging on the closed unit disc is $K\langle x\rangle$, and for $0 < r < 1$ the ring of Laurent series converging on the annulus $r \leq \lvert x \rvert < 1$ is $\mathcal{R}_r$.

## Differential Rings and Convergent Power Series

### The Ring of Convergent Series

**Definition.** Let $K\{x\}$ be the set of power series $f = \sum_{n \geq 0} a_n x^n$ with coefficients in $K$ and radius of convergence at least $1$, equivalently with $a_n \rho^n \to 0$ for every $\rho < 1$: the power series converging on the **open** unit disc. Let $K\langle x\rangle$ be the subset of those with $a_n \to 0$, the power series converging on the **closed** unit disc. The two differ only on the boundary circle, and $K\langle x\rangle \subseteq K\{x\}$ strictly, since $\sum_{n\geq0}x^n$ lies in the first and not in the second. For $0 < r < 1$ let $K\{x\}_r$ be the set of Laurent series $f = \sum_{n \in \mathbb{Z}} a_n x^n$ converging on the closed annulus $r \leq \lvert x \rvert \leq 1$; its union over $r$ is written $K\{x\}_{0,1}$.

**Proposition.** The sets $K\{x\}$, $K\langle x\rangle$ and $K\{x\}_{0,1}$ are $K$-algebras, and the derivation
$$
\partial\Bigl(\sum_{n \in \mathbb{Z}} a_n x^n\Bigr) = \sum_{n \in \mathbb{Z}} n\,a_n x^{n-1}
$$
is a $K$-linear derivation: $\partial(fg) = \partial(f)g + f\partial(g)$. The derivation preserves each of the rings and each of the annuli of convergence.

**Proof.** The ring structure is closed under addition and multiplication by the absolute convergence of the Cauchy product; the derivation is the formal derivative, and the Leibniz rule is checked on monomials and extended by the convergence of the double series. The radius of convergence is unchanged by differentiation, as was shown in *Analytic Functions and Power Series*, and the same computation on Laurent series gives the annulus statement. $\square$

The absence of an order in $K$ is irrelevant here: the derivation is defined by the coefficientwise formula and the Leibniz rule, and differentiation of a convergent series is legitimate at every interior point of its disc of convergence. This is the point at which the non-Archimedean theory is simpler than the real one, where the interchange of a limit and a derivative needs the mean value theorem.

### Differential Modules and the Equation $y' = Ay$

**Definition.** Let $S$ be a commutative $K$-algebra with a derivation $\partial$. A **differential module** over $S$ is a finitely generated $S$-module $M$ equipped with an additive map $\nabla : M \to M$ satisfying $\nabla(sm) = \partial(s)m + s\nabla(m)$ for $s \in S$, $m \in M$; the map $\nabla$ is a **connection**. A **morphism** of differential modules is an $S$-linear map commuting with the connections.

**Example (the equation $y' = Ay$).** Let $S = K\{x\}$ and let $A \in M_n(S)$. On the free module $M = S^n$ define $\nabla(y) = y' - Ay$, where the prime denotes the entrywise derivative. Then $\nabla$ is a connection: for $s \in S$ and $y \in S^n$, $\nabla(sy) = (sy)' - A(sy) = s'y + s y' - s A y = \partial(s)y + s\nabla(y)$. A **solution** of the equation $y' = Ay$ is an element $y \in S^n$ with $\nabla(y) = 0$, and a **fundamental solution matrix** is an $n \times n$ matrix $Y$ with $Y' = AY$ and $\det Y \neq 0$.

**Proposition (formal existence and uniqueness).** Let $A \in M_n(K[[x]])$ and let $y_0 \in K^n$. Then the equation $y' = Ay$ has a unique solution $y = \sum_{m \geq 0} y_m x^m$ in $K[[x]]^n$ with $y(0) = y_0$.

**Proof.** Comparing coefficients of $x^{m-1}$ in $y' = Ay$ gives $(m+1)y_{m+1} = \sum_{j=0}^{m} A_{m-j} y_j$, where $A = \sum_j A_j x^j$; the coefficient $m+1$ is a unit in $K$ because $K$ has characteristic $0$, so the recurrence determines $y_{m+1}$ uniquely from $y_0, \dots, y_m$. $\square$

The proposition is pure algebra and uses only characteristic $0$; what it does not assert is that the formal solution converges. The following example shows that convergence is a genuine restriction.

**Example (the exponential).** For $A = 1$ the solution with $y(0) = 1$ is $y = \exp x$, whose radius of convergence is $\rho_{\exp} = \lvert p \rvert^{1/(p-1)} < 1$ by *Analytic Functions and Power Series*. The coefficient $A = 1$ is the simplest possible entire function, and the solution nevertheless fails to converge on the open unit disc. The obstruction is the growth of the denominators $m!$ in the recurrence, which is a purely $p$-adic phenomenon.

## Convergence: Dwork's Lemma

### The General Estimate

**Proposition.** Let $A \in M_n(K\{x\}_r)$ with $\lVert A \rVert_{\mathrm{sup}} = c$ on the annulus $r \leq \lvert x \rvert \leq 1$, and let $y$ be the formal solution of $y' = Ay$ with $y(0) = y_0$. Then the radius of convergence of $y$ is at least $\min(1, \rho_{\exp}/c)$, in the sense that $y$ converges on every disc $\lvert x \rvert < \min(1, \rho_{\exp}/c)$.

**Proof sketch.** The recurrence of the existence proof gives, by induction, the bound on the coefficients of $y$ obtained from the corresponding bound for the solution of a scalar equation $y' = cy$, whose coefficients are $c^m/m!$; the non-Archimedean estimate $\lvert c^m/m! \rvert^{1/m} \to c/\rho_{\exp}$ gives the stated radius. The estimate is sharp for $A = c$ constant, where the solution is $\exp(cx)$ of radius $\rho_{\exp}/c$. $\square$

The estimate is crude because the denominators of the recurrence are $m+1$ rather than $m!$, and the true radius depends on the $p$-adic divisibility of the coefficients of $A$. The refined criterion is Dwork's lemma, which replaces the archimedean-looking estimate by an integrality condition.

### Dwork's Lemma

**Theorem (Dwork's lemma).** Let $f = \sum_{m \geq 0} a_m x^m \in \mathcal{O}[[x]]$ with $a_0 = 1$ and suppose that for some power $q = p^s$ of the residue characteristic the quotient
$$
\frac{f(x)}{f(x^q)} = \sum_{m \geq 0} b_m x^m
$$
has all its coefficients $b_m$ in $\mathcal{O}$. Then $f$ has all its coefficients in $\mathcal{O}$ and in particular converges on the open unit disc: $f \in K\{x\}$. The conclusion is not coefficient decay — $f = (1-x)^{-1}$ satisfies the hypothesis with $a_m = 1$ for every $m$ — and it is the integrality of the coefficients, not their decay, that the lemma supplies.

**Proof sketch.** The hypothesis gives $f(x) = f(x^q)\,g(x)$ with $g \in \mathcal{O}[[x]]$ of constant term $1$; iterating, $f(x) = f(x^{q^N})\prod_{i=0}^{N-1}g(x^{q^i})$ for every $N$, and letting $N\to\infty$ gives $f(x) = \prod_{i\geq0}g(x^{q^i})$ in $K[[x]]$, the product converging coefficientwise because the exponents $q^i$ tend to infinity and each coefficient of $f$ receives contributions from only finitely many factors. Each coefficient of the product is a finite sum of products of coefficients of $g$, hence has $\lvert \cdot \rvert \leq 1$ by the ultrametric inequality; so $\lvert a_m \rvert \leq 1$ for every $m$, which is convergence of $f$ on the open unit disc. $\square$

Dwork's lemma is the engine of the proof that the zeta function of a variety over a finite field is rational: it is applied to the series that solves a differential equation over a field of characteristic $p$ after lifting the coefficients, and it converts the divisibility of the quotients $f(x)/f(x^q)$ into the convergence needed to make sense of the analytic continuation. The arithmetic application belongs; the lemma is stated here because it is the first genuinely non-Archimedean convergence criterion for a differential equation and because the Robba ring of the next section is the natural home of its generalisations.

**Example (the geometric series).** For $f = (1-x)^{-1} = \sum_{m\geq0}x^m \in \mathcal{O}[[x]]$ one has $f(x)/f(x^p) = (1-x^p)/(1-x) = 1+x+\dots+x^{p-1} \in \mathcal{O}[x]$, so the hypothesis of the lemma holds and the conclusion is the convergence of $f$ on the open unit disc; the coefficients do not decay, since $a_m = 1$ for every $m$, which shows that the substance of the lemma is the integrality of the coefficients rather than their decay.

**Example (the Artin–Hasse exponential).** For the Artin–Hasse exponential $E_p$ of *Non-Archimedean Analysis* the identity $E_p(x)^p = E_p(x^p)\,e^{px}$ follows from the defining exponent $\sum_{k\geq0}x^{p^k}/p^k$ by multiplying it by $p$; it gives $E_p(x)/E_p(x^p) = e^{px}/E_p(x)^{p-1}$, and both factors lie in $\mathcal{O}[[x]]$, the second because a series of $\mathcal{O}[[x]]$ with constant term $1$ is invertible there. Dwork's lemma therefore recovers the convergence of $E_p$ on the open unit disc from an integrality statement rather than from the explicit product formula.

## The Robba Ring

### Definition and the Annulus Picture

**Definition.** The **Robba ring** is
$$
\mathcal{R} = \bigcup_{0 < r < 1} \mathcal{R}_r, \qquad \mathcal{R}_r = \Bigl\{ \sum_{n \in \mathbb{Z}} a_n x^n : \text{the series converges on } r \leq \lvert x \rvert < 1 \Bigr\},
$$
the ring of Laurent series that converge on some annulus with outer radius $1$ and inner radius $r > 0$. A series in $\mathcal{R}$ is **bounded** if its coefficients satisfy $\sup_n \lvert a_n \rvert < \infty$; the subring of bounded elements is written $\mathcal{R}^b$.

**Proposition.** $\mathcal{R}$ is a $K$-algebra containing $K\{x\}$ and $K[x^{-1}]$, closed under the derivation $\partial$, and it is an integral domain. A series belongs to $\mathcal{R}$ exactly when its coefficients satisfy $\lvert a_n \rvert \rho^{n} \to 0$ as $n \to +\infty$ for every $\rho > 1$ and $\lvert a_n \rvert r^{n} \to 0$ as $n \to -\infty$ for some $r < 1$.

**Proof.** Closure under addition and multiplication is convergence on a common smaller annulus. The stated convergence conditions are the non-Archimedean criterion applied to the two tails of a Laurent series; the ring is an integral domain because it is a subring of the field of formal Laurent series $K((x))$. Closure under $\partial$ is the preservation of the radius of convergence. $\square$

**Remark (the geometric picture).** Geometrically $\mathcal{R}_r$ is the ring of rigid analytic functions on the closed annulus $r \leq \lvert x \rvert \leq 1$ with the outer circle removed, in the sense; the Robba ring is the union of these rings as the inner radius shrinks to $0$, so it is the ring of functions analytic on a neighbourhood of the outer boundary circle of the disc and on the punctured disc. It is the $p$-adic analogue of the ring of germs of meromorphic functions at a punctured disc of the complex plane, and it is where the local analysis at a boundary point of the disc takes place.

### Lazard's Theorem

**Theorem (Lazard).** The Robba ring $\mathcal{R}$ is a Bézout domain: every finitely generated ideal of $\mathcal{R}$ is principal. Consequently every finitely generated torsion-free module over $\mathcal{R}$ is free, and every finitely generated module over $\mathcal{R}$ is a direct sum of a free module and a torsion module.

**Proof sketch.** The proof is by a sequence of reductions from the ring $\mathcal{R}_r$ to the ring of Laurent series, using the Weierstrass preparation theorem on the annulus: a nonzero element of $\mathcal{R}_r$ is, after multiplication by a unit and a power of $x$, a distinguished polynomial in a suitable variable, and the division by it is controlled by the preparation theorem. The Bézout property of the union then follows from the corresponding property at each radius. The structural consequences are the standard consequences of the Bézout property for a doma. $\square$

The Bézout property is what makes the Robba ring the correct analogue of a principal ideal domain and allows the structure theory of differential modules over it to be developed as in the classical theory of differential equations over $\mathbb{C}(x)$.

### The Frobenius and the Structure of $\mathcal{R}$

**Theorem.** The substitution $x \mapsto x^p$ defines an injective endomorphism $\varphi$ of $\mathcal{R}$ whose image is the subring $\mathcal{R}^{p}$ of series in $x^p$, and $\mathcal{R}$ is a finite free module over $\varphi(\mathcal{R})$ of rank $p$. The endomorphism $\varphi$ is a **Frobenius**, and the pair $(\mathcal{R},\varphi)$ is an example of a Frobenius ring in the sense of the theory of $\varphi$-modules.

**Proof.** The substitution is a ring homomorphism because it is induced by the map on the coefficient field; it is injective because a nonzero Laurent series has a nonzero image. A basis of $\mathcal{R}$ over its image is $1, x, \dots, x^{p-1}$, since every Laurent series is uniquely $\sum_{j=0}^{p-1} x^j f_j(x^p)$ with $f_j \in \mathcal{R}$; the convergence of the rearranged series is the non-Archimedean grouping criterion. $\square$

The Frobenius is the structure that links the differential theory to the arithmetic of the field of norms and to the theory of $\varphi$-modules and $(\varphi,\Gamma)$-modules; those applications belong to the arithmetic part of the corpus, and the analytic content used here is only the fact that the Frobenius makes $\mathcal{R}$ a finite module over its image.

## The Dwork–Robba Decomposition

### Slopes of a Differential Module

**Definition.** Let $M$ be a differential module over $\mathcal{R}$. A **sublattice** is a finitely generated $\mathcal{R}$-submodule $N \subseteq M$ with $\nabla(N) \subseteq N$; the module is **isoclinic of slope** $s \in \mathbb{Q}$ if it is nonzero and admits no nonzero sublattice of slope different from $s$, the slope of a rank-one module generated by $y$ being defined by the growth of the solutions of $y' = ay$ over the annulus.

The definition of the slope of a differential module over $\mathcal{R}$ makes precise the intuitive idea that solutions grow like $\lvert x \rvert^{-s}$ at the boundary; the slope is the $p$-adic analogue of the order of growth of a solution at a singular point, and it is computed by a Newton polygon attached to a basis of the module.

**Theorem (Dwork–Robba).** Let $M$ be a nonzero differential module over $\mathcal{R}$. Then $M$ admits a unique decomposition
$$
M = M_{>0} \oplus M_{\leq 0}
$$
into differential submodules, where $M_{>0}$ has all slopes $> 0$ and $M_{\leq 0}$ has all slopes $\leq 0$; more generally $M$ decomposes uniquely as a direct sum of isoclinic submodules of distinct slopes, and the slopes are rational numbers. The submodule of slope $0$ is the **unit-root part**, and it is the part whose solutions converge on the open unit disc.

**Proof sketch.** The theorem is proved by a successive approximation argument on the Newton polygon of a basis of $M$: one shows that a sublattice of maximal slope is a direct summand, and iterates; the rationality of the slopes follows from the Newton polygon having rational vertices, and the uniqueness from the maximality of the slope. The full proof is due to Dwork and Robba, and the modern account is that of Kedlaya; the essential input is the Bézout property of $\mathcal{R}$ and the Frobenius. $\square$

**Corollary (the unit-root part and convergence).** A differential module over $\mathcal{R}$ of slope $0$ has all its solutions bounded on the annulus and analytic on the open unit disc; a module of positive slope has solutions that grow like a negative power of $\lvert x \rvert$, hence are not analytic at $0$.

The decomposition is the $p$-adic replacement for the classification of singularities of a linear differential equation at a point of $\mathbb{C}$: the slope plays the role of the order of the pole, and the unit-root part plays the role of the regular singular part with trivial exponents.

## The Fuchsian Case and Solvability at a Boundary Point

### The Formal Fuchs Theorem

**Theorem (formal Fuchs theorem).** Let $B \in M_n(K)$ and consider the equation $xy' = By$. Then there is a formal fundamental solution
$$
Y(x) = F(x)\,x^B, \qquad F \in \mathrm{GL}_n(K[[x]]), \quad F(0) = I,
$$
where $x^B$ is defined by the formal logarithm of the matrix, and the expansion is valid in a finite extension of $K$ if the eigenvalues of $B$ are not all in $K$.

**Proof sketch.** The matrix $x^B = \exp(B \log x)$ is defined by the finite-dimensional linear algebra of $B$: if $B$ is in Jordan form, $x^B$ is assembled from the powers $x^{\alpha}(\log x)^k$ for the eigenvalues $\alpha$ of $B$ and the sizes of its Jordan blocks. Substituting $Y = Fx^B$ into the equation gives $xF' = BF - FB$, an equation for $F$ with a regular singularity of the second kind whose formal solution is obtained by the recurrence of the existence theorem; the resonance conditions are automatically satisfied in the formal setting. $\square$

### The $p$-adic Fuchs Criterion

**Remark (convergence of the Fuchsian solution).** The formal solution $F$ of the Fuchs theorem need not converge on the open unit disc, and the criterion that decides its convergence is arithmetic: it depends on the $p$-adic valuations of the differences $\alpha_i - \alpha_j$ of the eigenvalues of $B$ and on the ramification of the eigenvalue field. The criterion is Dwork's $p$-adic Fuchs theorem: the solution $Y = Fx^B$ converges on the open unit disc precisely when the eigenvalue differences satisfy the valuations required by the convergence of the exponential series appearing in the formal logarithm; the statement requires the eigenvalues to be sufficiently $p$-adically separated, and it is sharp. The precise formulation and its proof are in the standard literature, to which the reader is referred; the version for a general differential module over $\mathcal{R}$ is the statement that the module is **solvable at $1$** when all of its slopes are $\geq 0$.

**Definition.** A differential module $M$ over $\mathcal{R}$ is **solvable at the boundary** (or **solvable at $1$**) if its slopes are all $\geq 0$; equivalently if the module of solutions has moderate growth at the outer boundary circle. A formal differential equation over $K(x)$ with a singularity at the boundary is solvable there when its associated $\mathcal{R}$-module is.

**Proposition.** A differential module over $\mathcal{R}$ is solvable at the boundary if and only if all its slopes are $\geq 0$, that is, if and only if none of its isoclinic pieces has negative slope. The property is stable under extension of scalars and under the formation of tensor products and duals.

**Proof sketch.** The slope decomposition reduces the statement to the isoclinic case, where the slope of the module is the negative of the growth exponent of the solutions at the boundary and solvability is the statement that the exponent is nonpositive. Stability is checked on the Newton polygons. $\square$

## Algebraic Series and the Christol–Dwork Criterion

### Christol's Theorem

**Theorem (Christol).** Let $q = p^s$ and let $f = \sum_{m \geq 0} a_m x^m \in \mathbb{F}_q[[x]]$. Then $f$ is algebraic over $\mathbb{F}_q(x)$ if and only if the sequence $(a_m)$ is $p$-automatic, that is, if and only if the set of subsequences obtained by extracting the coefficients along the arithmetic progressions $m \mapsto p^r m + c$ is finite.

**Proof sketch.** If $f$ is algebraic, the vector space over $\mathbb{F}_q$ spanned by $f$ and its iterated Cartier transforms $C(f) = \sum_m a_{pm+1} x^m$ is finite-dimensional, and the finiteness of the set of subsequences follows; conversely, a finite-dimensional Cartier-stable span produces a linear relation over $\mathbb{F}_q(x)$, which is an algebraic equation. $\square$

### The Criterion over a $p$-adic Field

**Theorem (Dwork).** Let $K$ be a finite extension of $\mathbb{Q}_p$ and let $f \in K[[x]]$ be algebraic over $K(x)$. Then $f$ converges on the open unit disc and the differential module over the Robba ring associated with $f$ is solvable at the boundary.

**Proof sketch.** An algebraic function satisfies a linear differential equation with coefficients in $K(x)$, by the finiteness of the span of its derivatives over $K(x)$; the equation has at worst a regular singularity at the boundary circle after a change of variable, and the associated differential module over $\mathcal{R}$ therefore has all its slopes $\geq 0$. The detailed computation of the slopes is a case of the theory of regular singular equations of the preceding section. $\square$

**Remark (the converse).** The converse — that a power series convergent on the open unit disc whose differential module over $\mathcal{R}$ is solvable at the boundary, and whose reduction satisfies an algebraic equation over the residue field, is algebraic over $K(x)$ — is the criterion of Christol and Dwork. Its proof transposes Christol's automaton argument from the finite field to the $p$-adic setting: the solvability at the boundary makes the module generated by $f$ and its iterated derivatives finite over the Robba ring, the Frobenius and the Cartier operators cut it down to a finite-dimensional span stable under the Cartier action, and a finite-dimensional Cartier-stable span produces a linear relation over $K(x)$, hence an algebraic equation. The additional hypotheses on the reduction are necessary and are stated in the literature; the criterion is cited here rather than proved.

The criterion is the bridge between the analytic theory of this article and the arithmetic of the zeta functions: the rationality of the zeta function of a variety over a finite field is proved by associating to it a differential equation whose differential module over $\mathcal{R}$ is solvable at the boundary, and the resulting convergence and algebraicity statements are the analytic input of the pro. The arithmetic applications, and the zeta functions themselves, belong .

## Summary

The differential equations of the $p$-adic theory are the equations $y' = Ay$ with $A$ a matrix of convergent power series, and a differential module over a ring of convergent series is a finite free module with a connection. The formal theory is complete: the equation has a unique formal solution with prescribed initial value, because the recurrence divides by the integers $m+1$, which are invertible in characteristic zero. Convergence is the genuinely $p$-adic question, and it can fail: the solution of $y' = y$ is the exponential, of radius $\lvert p \rvert^{1/(p-1)}$ although the coefficient is constant. Dwork's lemma converts the integrality of the quotients $f(x)/f(x^q)$ into convergence on the open unit disc and is the standard convergence criterion of the theory.

The Robba ring, the union over $r>0$ of the rings of Laurent series converging on the annulus $r \leq \lvert x \rvert < 1$, is the natural home of the local theory at the boundary of the disc. It is a Bézout domain by Lazard's theorem, it carries the Frobenius $x \mapsto x^p$ that makes it a finite free module of rank $p$ over its image, and every differential module over it decomposes uniquely into isoclinic pieces whose slopes are rational. The unit-root part has slope $0$ and its solutions are analytic on the open unit disc; the modules of negative slope are exactly those that fail to be solvable at the boundary. In the Fuchsian case $xy' = By$ the formal solution is $Fx^B$, and the convergence of $F$ is decided by the $p$-adic separation of the eigenvalues of $B$, which is Dwork's $p$-adic Fuchs criterion. Finally, the Christol–Dwork criterion characterises the algebraic power series among those convergent on the open unit disc by the solvability at the boundary of their differential module, and Christol's theorem characterises them over a finite field by the $p$-automaticity of their coefficients; this is the point at which the analytic theory feeds back into arithmetic.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Complete non-Archimedean field of characteristic $0$ |
| $\lvert \cdot \rvert$, $v$ | Absolute value and valuation |
| $\mathcal{O}$, $\mathfrak{m}$, $k$ | Valuation ring, maximal ideal, residue field of characteristic $p$ |
| $\rho_{\exp} = \lvert p \rvert^{1/(p-1)}$ | Radius of convergence of the exponential |
| $\partial$, $'$ | The derivation $d/dx$ |
| $K[[x]]$, $K\{x\}$, $K\langle x\rangle$ | Formal series, series convergent on the open unit disc, on the closed unit disc |
| $K\{x\}_{0,1}$, $\mathcal{R}_r$ | Laurent series convergent on an annulus $r \leq \lvert x \rvert < 1$ |
| $\mathcal{R}$ | Robba ring, $\bigcup_{0<r<1}\mathcal{R}_r$ |
| $\mathcal{R}^b$ | Bounded elements of the Robba ring |
| $\nabla$ | Connection of a differential module |
| $y' = Ay$ | Linear differential system, $A \in M_n$ |
| $Y$, $F$, $x^B$ | Fundamental solution, Fuchsian factor, formal power of $x$ |
| $\varphi : x \mapsto x^p$ | Frobenius endomorphism of $\mathcal{R}$ |
| slope, isoclinic | Slope of a differential module, and its isoclinic pieces |
| $M_{>0}$, $M_{\leq 0}$ | Positive-slope part and nonpositive-slope part |
| solvable at $1$ | All slopes $\geq 0$ |
| $q = p^s$ | A power of the residue characteristic |
| $p$-automatic | Sequence generated by a finite automaton reading base-$p$ digits |
| $M_n(S)$ | $n \times n$ matrices over $S$ |



## Further Reading

- Bernard Dwork, *On the rationality of the zeta function of an algebraic variety* (American Journal of Mathematics 82, 1960), for Dwork's lemma and the analytic proof of rationality.
- Philippe Robba, *On the index of $p$-adic differential operators I* (Duke Mathematical Journal 43, 1976), for the Robba ring and the structure of its differential modules.
- Kiran S. Kedlaya, *$p$-adic Differential Equations* (Cambridge University Press, 2010), for the modern systematic treatment, the slope decomposition and the Fuchs criteria.
- Gilles Christol, *Ensembles presque périodiques $k$-reconnaissables* (Theoretical Computer Science 9, 1979), for the automaton characterisation of algebraic series over a finite field.
- Bernard Dwork, Giovanni Gerotto and Francis J. Sullivan, *An Introduction to $G$-Functions* (Princeton University Press, 1994), for the analytic theory of differential equations over a $p$-adic field.
- Michel Lazard, *Les zéros des fonctions analytiques d'une variable sur un corps valué complet* (Publications Mathématiques de l'IHÉS 14, 1962), for the Bézout property of the ring of convergent Laurent series.
- Amnon Yekutieli, *An Explicit Construction of the Grothendieck Residue Complex* (Astérisque 208, 1992), for the algebraic theory of differential modules over annuli.
- Siegfried Bosch, *Lectures on Formal and Rigid Analytic Geometry* (Springer, 2014), for the rigid analytic geometry of annuli underlying the Robba ring.
