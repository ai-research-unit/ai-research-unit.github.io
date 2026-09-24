
# __Rigid Analytic Functions__

## Introduction

A rigid analytic function is a function on a rigid analytic space that is locally a quotient of convergent power series. The spaces themselves — the affinoid spaces, the admissible opens and the Grothendieck topology that makes them glue — belong to Part II, in *Rigid Analytic Geometry* and *Berkovich Spaces*; this article is the theory of the functions on them. The subject begins with the observation that the naive topology of a non-Archimedean field is useless for analytic continuation: the closed unit disc is the disjoint union of the cosets of $p\mathbb{Z}_p$, so a function that is a power series on the disc and another on the annulus outside it do not glue by ordinary open sets, and the classical theorem that a function analytic on a disc is determined by its germ fails to have a home. Tate's remedy was to allow only certain covers — the admissible covers by rational subdomains — and to prove that the presheaf of convergent power series on them is a sheaf. The resulting objects have a function theory of their own, and it is strikingly rigid: the maximum modulus principle holds with a multiplicative norm, there are no bump functions, a nonconstant function cannot be flat at a point to infinite order without vanishing, and the reduction to the residue field turns the local study into commutative algebra over $k$.

This article develops that function theory. It defines the Tate algebra with its Gauss norm, proves the Gauss lemma (multiplicativity of the norm) and the Weierstrass division and preparation theorems, states the maximum modulus principle, defines affinoid algebras and their spectra, records Tate's acyclicity theorem and the Nullstellensatz, and treats the rigidity phenomena — the identity theorem on connected spaces, the absence of partitions of unity, the sup-norm formula, the non-Archimedean Liouville theorem and Krasner's lemma. It closes with the standard examples: the closed unit disc with its reduction to the affine line over the residue field, the annuli, the unit circle as a Laurent domain, and the punctured disc, whose ring of analytic functions is the Robba ring of *p-adic Differential Equations*.

The prerequisites are *Analytic Functions and Power Series* and *Non-Archimedean Analysis* for convergent series and the ultrametric estimates, *p-adic Analysis* for the unit disc and the Newton polygon, *p-adic Differential Equations* for the Robba ring, *Rings* and *Modules* for Noetherian rings and localisation, and *Rigid Analytic Geometry*, written in parallel, for the spaces and the Grothendieck topology; the comparison with the complex theory is the business of the synthetic study of $\mathbb{C}$, and the Berkovich and adic points of view are in *Berkovich Spaces* and *Adic Spaces*. Throughout, $K$ is a complete non-Archimedean field with absolute value $\lvert \cdot \rvert$, valuation ring $K^\circ$, maximal ideal $K^{\circ\circ}$ and residue field $\tilde K = k$; the field is algebraically closed when a statement needs it, and this is flagged. The unit polydisc is the set of $x = (x_1,\dots,x_n)$ with all $\lvert x_i \rvert \leq 1$, and the Gauss norm of a series is the supremum of the absolute values of its coefficients.

## The Tate Algebra

### Definition and the Gauss Norm

**Definition.** The **Tate algebra** in $n$ variables over $K$ is
$$
T_n = K\langle \xi_1, \dots, \xi_n \rangle = \Bigl\{ f = \sum_{\nu \in \mathbb{N}^n} a_\nu \xi^\nu : a_\nu \in K,\ \lvert a_\nu \rvert \to 0 \Bigr\},
$$
the ring of power series in $n$ variables whose coefficients tend to $0$; the **Gauss norm** of $f$ is $\lVert f \rVert = \max_\nu \lvert a_\nu \rvert$, the maximum existing because the coefficients tend to $0$. The **reduction** of $f$ is $\tilde f = \sum_{\nu : \lvert a_\nu \rvert = \lVert f \rVert} \bar a_\nu \xi^\nu \in k[\xi_1,\dots,\xi_n]$, the sum over the coefficients of maximal absolute value, taken modulo the maximal ideal.

**Theorem (Gauss).** $T_n$, with the Gauss norm, is a $K$-Banach algebra, and the Gauss norm is multiplicative:
$$
\lVert fg \rVert = \lVert f \rVert\,\lVert g \rVert \qquad (f, g \in T_n).
$$
Moreover $\tilde{fg} = \tilde f \tilde g$ with equality of degrees, so that $T_n$ has no zero divisors and $k[\xi] \to \tilde T_n$ is an isomorphism onto the reduction.

**Proof.** Submultiplicativity of the Gauss norm is immediate from the ultrametric inequality on the coefficients of a product. For multiplicativity, scale so that $\lVert f \rVert = \lVert g \rVert = 1$; then $f, g$ lie in the subring $T_n^\circ$ of series with coefficients in the valuation ring $K^\circ$, and reduction modulo the maximal ideal gives a ring isomorphism $T_n^\circ/\mathfrak{m}T_n^\circ \cong k[\xi_1,\dots,\xi_n]$, since a series with coefficients in $K^\circ$ determines and is determined by its reduction. The reductions $\tilde f, \tilde g$ are nonzero, and $k[\xi]$ is a polynomial ring over a field, hence a domain, so $\widetilde{fg} = \tilde f\tilde g \neq 0$ and therefore $\lVert fg \rVert = 1 = \lVert f \rVert \lVert g \rVert$. The general case follows by scaling. The statement about the reduction is the same computation. $\square$

The multiplicativity of the Gauss norm is the technical heart of the theory: it is what makes the affinoid algebras behave like rings of functions with a sup norm, and it fails in the Archimedean case, where the analogous norm on the disc algebra is only submultiplicative.

### Weierstrass Division and Preparation

**Definition.** A series $f \in T_n$ is **distinguished of degree** $d$ in $\xi_n$ if its terms of maximal absolute value form a polynomial of degree $d$ in $\xi_n$, monic of degree $d$ in the reduction. More precisely, $f \in T_n$ of norm $1$ is distinguished of degree $d$ if $\tilde f \in k[\xi]$ has degree $d$ as a polynomial in $\xi_n$ and the coefficient of $\xi_n^d$ in $\tilde f$ is nonzero; the coefficient of $\xi_n^d$ in $f$ is then a unit and the other coefficients of $\xi_n$-degree $> d$ have norm less than $1$.

**Theorem (Weierstrass division).** Let $f \in T_n$ be distinguished of degree $d$ in $\xi_n$, normalised to $\lVert f \rVert = 1$. Then for every $g \in T_n$ there are unique $q \in T_n$ and $r \in T_{n-1}[\xi_n]$ with $\deg_{\xi_n} r < d$ and
$$
g = qf + r.
$$
**Proof sketch.** The division is performed coefficient by coefficient in $\xi_n$, using the invertibility of the leading coefficient of $f$ as a power series in $\xi_1,\dots,\xi_{n-1}$ up to smaller terms: one writes $f = \xi_n^d c + (\text{lower terms})$ with $c$ a unit of $T_{n-1}$, solves successively for the coefficients of $q$ and $r$ in decreasing $\xi_n$-degree, and shows that the successive corrections tend to $0$ in the norm, so that the process converges in the Banach algebra. Uniqueness follows from the shape of $r$. $\square$

**Theorem (Weierstrass preparation).** Let $f \in T_n$ be distinguished of degree $d$ in $\xi_n$. Then $f$ factors uniquely as
$$
f = u \cdot P, \qquad P = \xi_n^d + c_{d-1}\xi_n^{d-1} + \cdots + c_0,
$$
with $u$ a unit of $T_n$ and $c_i \in T_{n-1}$ of norm $< 1$; the polynomial $P$ is a **Weierstrass polynomial**.

**Proof.** Apply the division theorem to $g = \xi_n^d$ and to $f$; the remainder is a polynomial in $\xi_n$ of degree $< d$ with coefficients in $T_{n-1}$, and the standard argument identifies $u^{-1}$ with the quotient and $P$ with $\xi_n^d - r$. The convergence of the division is the content of the previous theorem. $\square$

**Corollary (the Tate algebra is Noetherian).** The ring $T_n$ is Noetherian, and if $A = T_n/\mathfrak{a}$ is a quotient, then $A$ is Noetherian.

**Proof.** The preparation theorem reduces the Noetherian property of $T_n$ to that of $T_{n-1}$: an ideal of $T_n$ is generated by finitely many elements after division by a distinguished element, and the induction on $n$ starts from the field $T_0 = K$. $\square$

### The Maximum Modulus Principle

**Theorem (maximum modulus principle).** Let $\bar K$ be the completion of an algebraic closure of $K$, with valuation ring $\bar K^\circ$, and let $T_n(\bar K) = \bar K\langle \xi_1,\dots,\xi_n\rangle$ be the corresponding Tate algebra. For $f \in T_n(\bar K)$,
$$
\lVert f \rVert = \sup_{x \in (\bar K^\circ)^n} \lvert f(x) \rvert,
$$
and the supremum is attained at some point of the unit polydisc; in particular a series of norm $1$ attains the value $1$ on the polydisc.

**Proof sketch.** Over an algebraically closed residue field, one uses the Weierstrass preparation theorem to reduce, by successive subtraction of Weierstrass polynomials and an induction on $n$, to the case of a distinguished polynomial of degree $d$ in one variable: the Weierstrass polynomial has $d$ roots of absolute value $\leq 1$ in $\bar K$ by the Newton polygon, and evaluating at one of them realises the leading coefficient. The passage to a general residue field is by a finite extension, the norm of the extension being a finite power of the original absolute value. $\square$

**Corollary (the spectral norm).** For $f \in T_n$ the formula $\lVert f \rVert = \lim_m \lVert f^m \rVert^{1/m}$ holds, so the Gauss norm is the spectral norm of $f$ in the sense of Banach algebras; equivalently, $\lVert f \rVert = \sup_{x \in (\bar K^\circ)^n} \lvert f(x) \rvert$ and $\lVert f^m \rVert = \lVert f \rVert^m$ for all $m$. The supremum is taken over the points of the polydisc in $\bar K$: over a field with finite residue field the supremum over the points of the ground field alone can be strictly smaller, as the example $x + x^2$ over $\mathbb{Q}_2$ shows.

**Proof.** The sup formula and the multiplicativity of the Gauss norm give both statements at once; the limit formula is the general relation between the spectral radius and the sup norm for a commutative Banach algebra over $\bar K$. $\square$

## Affinoid Algebras and their Spectra

### Definitions

**Definition.** A **$K$-affinoid algebra** is a $K$-Banach algebra $A$ that is a quotient $T_n/\mathfrak{a}$ of a Tate algebra by a closed ideal, with the quotient norm; the **spectrum** $\mathrm{Spm}(A) = X$ is the set of maximal ideals of $A$ with the topology generated by the sets $\{x : \lvert f(x) \rvert \leq 1\}$, and the **sup norm** on $A$ is
$$
\lVert f \rVert_{\mathrm{sup}} = \sup_{x \in \mathrm{Spm}(A)} \lvert f(x) \rvert,
$$
where $\lvert f(x) \rvert$ is the absolute value of the image of $f$ in the residue field $A/\mathfrak{m}_x$, completed if necessary. The **spectral norm** is $\lVert f \rVert_{\mathrm{sp}} = \lim_m \lVert f^m \rVert^{1/m}$.

**Theorem (properties of affinoid algebras).** Let $A$ be a $K$-affinoid algebra. Then $A$ is Noetherian, Jacobson, and complete with respect to its norm; its maximal ideals have finite residue fields over $K$; and if $K$ is algebraically closed, the residue field at every maximal ideal is $K$, so that every maximal ideal is determined by the evaluation of the coordinate functions at a point of $(K^\circ)^n$ after the choice of a presentation.

**Proof.** Noetherianness descends from the Tate algebra; the Jacobson property is proved by the Nullstellensatz for affinoid algebras, which identifies the maximal ideals with the kernels of the evaluation maps to finite extensions of $K$ and shows that a function vanishing at all maximal ideals is nilpotent. Completeness is the completeness of the quotient of a Banach space by a closed subspace. $\square$

**Theorem (maximum modulus principle for affinoid algebras; Tate).** Let $K$ be algebraically closed and let $A$ be a reduced $K$-affinoid algebra. Then the spectral norm equals the sup norm, $\lVert f \rVert_{\mathrm{sp}} = \lVert f \rVert_{\mathrm{sup}}$ for every $f \in A$, and the spectrum is a nonempty set on which the supremum is attained.

**Proof sketch.** Choose a presentation $A = T_n/\mathfrak{a}$ and lift $f$ to $\hat f \in T_n$; the sup norm of $f$ on $\mathrm{Spm}(A)$ is the infimum of $\lVert \hat f + g \rVert$ over $g \in \mathfrak{a}$ with the Gauss norm on the right, and the equality of the two norms is proved by the maximum modulus principle of the Tate algebra together with the fact that the reduction is reduced; the attainment follows from the compactness of the spectrum in the relevant sense. This is the central theorem of the analytic theory of affinoid algebras. $\square$

### Tate's Acyclicity and the Structure Sheaf

**Definition.** A **Weierstrass domain** of $X = \mathrm{Spm}(A)$ is a subset of the form $\{x : \lvert f_1(x) \rvert \leq 1, \dots, \lvert f_r(x) \rvert \leq 1\}$ for $f_i \in A$; a **Laurent domain** adds conditions $\lvert g_j(x) \rvert \geq 1$ with $g_j \in A$; a **rational domain** is defined by conditions of the form $\lvert f_i(x) \rvert \leq \lvert g(x) \rvert$ for a single $g$. The **affinoid algebra of the domain** is the completion of $A$ with respect to the generators and the inverse of $g$; a finite cover by rational domains is an **admissible cover**.

**Theorem (Tate's acyclicity theorem).** Let $X = \mathrm{Spm}(A)$ be an affinoid space and let $\mathfrak{U} = \{U_i\}$ be an admissible cover by rational domains, with $A_i$ the affinoid algebra of $U_i$. Then the sequence
$$
0 \longrightarrow A \longrightarrow \prod_i A_i \longrightarrow \prod_{i,j} A_{ij} \longrightarrow \cdots
$$
is exact, where $A_{ij\cdots}$ is the affinoid algebra of the intersection; that is, the presheaf $U \mapsto A_U$ is a sheaf for the Grothendieck topology generated by the admissible covers, and the covers are acyclic.

**Proof sketch.** The exactness is proved first for a Laurent cover of the unit polydisc by the two domains $\lvert \xi_1 \rvert \leq 1$ and $\lvert \xi_1 \rvert \geq 1$, where it reduces to the splitting of a Laurent series into its nonnegative and negative parts, and is then propagated to rational covers and to products by the Weierstrass preparation. The general case is by the standard reduction to the two-element cover. $\square$

The theorem is what licenses the construction of global rigid analytic spaces by gluing affinoids, which is carried out in *Rigid Analytic Geometry*; from the point of view of this article it says that the ring of rigid analytic functions on an affinoid space is $A$ itself and that the functions are determined by their restrictions to an admissible cover.

## Rigidity Phenomena

### The Identity Theorem on Connected Spaces

**Definition.** A rigid analytic space $X$ is **connected** if it is not the disjoint union of two nonempty admissible open subsets; the closed unit disc, the polydiscs, the annuli $r \leq \lvert x \rvert \leq 1$ and the unit circle are connected, while the disc minus a point is not.

**Theorem (rigidity of analytic continuation).** Let $X$ be a connected rigid analytic space and let $f \in \mathcal{O}(X)$ be a rigid analytic function on $X$. If $f$ vanishes on a nonempty admissible open subset of $X$, then $f = 0$ on $X$.

**Proof.** The statement is local: on a connected affinoid, $f$ is given by a power series on a neighbourhood of a point, and the identity theorem of *Analytic Functions and Power Series* shows that the set where $f$ vanishes to infinite order at a point of a fixed affinoid is both admissible open and admissible closed; connectedness forces it to be everything. Gluing over the admissible cover of $X$ gives the global statement. $\square$

**Corollary (no bump functions).** There is no nonzero rigid analytic function on the closed unit disc that vanishes identically outside a proper subdomain of it; more generally the sheaf $\mathcal{O}$ has no nonzero sections with compact support, and there is no partition of unity subordinate to a nontrivial admissible cover.

**Proof.** A function supported in a proper subdomain vanishes on the complement, which contains a nonempty admissible open set, so the identity theorem forces it to vanish. For partitions of unity one observes that the sum of a finite family of analytic functions equal to $1$ on the disc and supported in the members of a cover would give a bump function. $\square$

### The Sup Norm and the Liouville Theorem

**Theorem (non-Archimedean Liouville theorem).** Let $f = \sum_{m \geq 0} a_m x^m$ be an entire rigid analytic function on the affine line, that is, a series converging on every closed disc. If $f$ is bounded, $\sup_x \lvert f(x) \rvert < \infty$, then $f$ is constant.

**Proof.** Convergence on every closed disc means $\lvert a_m \rvert \rho^m \to 0$ for every $\rho$, hence $\lvert a_m \rvert^{1/m} \to 0$. Suppose some $a_m \neq 0$ with $m \geq 1$ and let $m$ be minimal among such; for a point $x$ of sufficiently large absolute value the term $a_m x^m$ has absolute value exceeding all the others, by the convergence of the tail and the finiteness of the head, so $\lvert f(x) \rvert = \lvert a_m \rvert \lvert x \rvert^m$ is unbounded. Hence all $a_m = 0$ for $m \geq 1$. $\square$

The Liouville theorem is the sharpest expression of the discrepancy with the complex theory: over $\mathbb{C}$ the bounded entire functions are constant, and the classical proof needs the maximum modulus principle applied on circles of arbitrarily large radius and the identity theorem, whereas here the same conclusion follows from the elementary observation that for $\lvert x \rvert$ large a single term of the series dominates and makes $\lvert f(x) \rvert$ grow without bound. There is no analogue of the classical theorem that a bounded analytic function on the disc has boundary values, since the boundary circle is not a real curve and carries no measure of the type used there.

### Krasner's Lemma

**Lemma (Krasner).** Let $K$ be a complete non-Archimedean field and let $\alpha, \beta$ lie in an algebraic closure with $\lvert \beta - \alpha \rvert < \lvert \beta - \alpha' \rvert$ for every conjugate $\alpha' \neq \alpha$ of $\alpha$ over $K$. Then $\alpha \in K(\beta)$.

**Proof sketch.** The conjugates of $\beta$ over $K(\alpha,\beta)$ are of the form $\sigma(\beta)$ and one shows $\lvert \beta - \sigma(\alpha) \rvert = \lvert \beta - \alpha \rvert$ for the relevant $\sigma$; the strict inequality forces every $K$-embedding of $K(\alpha,\beta)$ fixing $\beta$ to fix $\alpha$, whence $\alpha \in K(\beta)$. $\square$

**Corollary (analytic continuation of roots).** Let $\sum_{i} a_i(x) t^i$ be a polynomial in $t$ whose coefficients are rigid analytic functions of $x$ on a connected affinoid, with $\lvert a_0(x) \rvert$ bounded below by a positive constant on the domain. Then the multiset of roots of the polynomial varies rigidly: two roots that coincide at one point coincide on the whole domain, and the roots are rigid analytic functions of $x$ after passing to a finite extension of the base.

**Proof.** The roots are algebraic functions of $x$; at a point where two roots are distinct, their difference has a definite absolute value, and Krasner's lemma applied along the connected domain shows that the discriminant cannot change sign. The analytic dependence is the standard consequence of the implicit function theorem for affinoid algebras. $\square$

## Examples

**Example (the closed unit disc and its reduction).** The closed unit disc over $K$ is the affinoid space $X = \mathrm{Spm}(T_1)$ with $T_1 = K\langle \xi\rangle$. Its reduction is $\tilde T_1 = k[\xi]$, and the reduction map
$$
X \longrightarrow \mathbb{A}^1_k, \qquad x \longmapsto \tilde x = \text{the reduction of the coordinate of } x,
$$
is surjective and has as fibres the residue classes of the disc. A function $f \in T_1$ of norm $1$ that is a unit has reduction $\tilde f$ a nonzero polynomial, and $f$ attains the value $1$ on the disc by the maximum modulus principle. The disc is connected and its functions are the power series with coefficients tending to $0$.

**Example (annuli and the unit circle).** For $0 < r < 1$ the annulus $A(r,1) = \{x : r \leq \lvert x \rvert \leq 1\}$ is the affinoid space of the Laurent domain defined by $\lvert x \rvert \leq 1$ and $\lvert x \rvert \geq r$, with affinoid algebra $K\langle r x^{-1}, x\rangle$, the ring of Laurent series $\sum_{n\in\mathbb{Z}} a_n x^n$ with $\lvert a_n \rvert r^n \to 0$ for $n \to -\infty$ and $\lvert a_n \rvert \to 0$ for $n \to +\infty$. The unit circle $\lvert x \rvert = 1$ is the rational domain defined by $\lvert x \rvert = 1$, with algebra the Laurent algebra $K\langle x, x^{-1}\rangle$. As $r$ decreases to $0$ the algebras $K\langle r x^{-1}, x\rangle$ increase, and no single affinoid algebra among them is the ring of all functions on the punctured disc.

**Example (the punctured disc and the Robba ring).** The ring of rigid analytic functions on the punctured open unit disc is
$$
\mathcal{R} = \bigcup_{0 < r < 1} K\{x\}_{r},
$$
the Robba ring of *p-adic Differential Equations*: a function on the punctured disc restricts to an annulus $r \leq \lvert x \rvert < 1$ for some $r$, and every element of the union arises. The punctured disc is the standard example of an admissible open that is not affinoid, and the ring $\mathcal{R}$ is not a Banach algebra, which is why the differential theory over it needs the extra structure of the slope decomposition.

**Example (the disc has no nonconstant bounded functions of a special shape).** For $K = \mathbb{Q}_p$ the function $f(x) = \sum_{m \geq 0} p^{m} x^{m}$ converges exactly on the open unit disc and is unbounded there, while the function $g(x) = \sum_{m\ge0} p^{m} x^{m^2}$ converges on the closed unit disc with $\lVert g \rVert = 1$ and attains the value $1$ at $x = 0$. There is no entire function on the affine line that is bounded and nonconstant, by the Liouville theorem above.

## Summary

Rigid analytic functions are the local quotients of convergent power series on the admissible opens of a rigid analytic space, and the theory of this article is the function theory that the spaces of Part II support. The Tate algebra $T_n = K\langle\xi_1,\dots,\xi_n\rangle$, the power series with coefficients tending to $0$, is a Banach algebra whose Gauss norm is multiplicative, hence is the sup norm on the unit polydisc; the multiplicativity is the Gauss lemma and is the source of the rigidity of the whole theory. The Weierstrass division and preparation theorems hold in $T_n$ with the same statements as over a complex disc, and they give the Noetherian property of the Tate algebra. An affinoid algebra is a quotient of a Tate algebra, its spectrum is a rigid analytic space, and its elements are the rigid analytic functions on it.

The maximum modulus principle, $\lVert f \rVert = \sup_{x \in (\bar K^\circ)^n} \lvert f(x) \rvert$ with the supremum attained, holds for the Tate algebra and, for reduced affinoid algebras over an algebraically closed field, in the form spectral norm $=$ sup norm. Tate's acyclicity theorem makes the assignment $U \mapsto A_U$ a sheaf for the Grothendieck topology of admissible covers, so that functions are determined locally and glue along admissible covers. The rigidity of the theory follows: on a connected rigid analytic space a function vanishing on a nonempty admissible open vanishes identically, there are no bump functions and no partitions of unity, a bounded entire function on the affine line is constant, and the roots of a polynomial family cannot cross without coinciding on the whole connected domain, by Krasner's lemma. The examples of the closed disc and its reduction, the annuli, the unit circle and the punctured disc with its Robba ring show how the general theory specialises, and the last of these is the link to the differential theory of *p-adic Differential Equations*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Complete non-Archimedean field |
| $\bar K$, $\bar K^\circ$ | Completed algebraic closure, its valuation ring |
| $k = \tilde K$ | Residue field of $K$ |
| $T_n = K\langle \xi_1,\dots,\xi_n\rangle$ | Tate algebra in $n$ variables |
| $\lVert f \rVert$ | Gauss norm, maximum of the coefficient absolute values |
| $\tilde f$ | Reduction of $f$, a polynomial over $k$ |
| $K\langle r x^{-1}, x\rangle$ | Affinoid algebra of the annulus $r \leq \lvert x \rvert \leq 1$ |
| $A$ | A $K$-affinoid algebra, a quotient of $T_n$ |
| $\mathrm{Spm}(A)$ | Spectrum of maximal ideals, the affinoid space |
| $\lVert f \rVert_{\mathrm{sup}}$, $\lVert f \rVert_{\mathrm{sp}}$ | Sup norm and spectral norm on $A$ |
| $\mathcal{O}(X)$, $\mathcal{O}_X$ | Ring of rigid analytic functions on $X$, structure sheaf |
| Weierstrass, Laurent, rational domain | The admissible affinoid subdomains |
| Admissible cover | A finite cover by rational domains |
| $A(r,1)$ | The annulus $r \leq \lvert x \rvert \leq 1$ |
| $\mathcal{R}$ | Robba ring, functions on the punctured open disc |
| $\lvert \cdot \rvert_p$ | The $p$-adic absolute value, $\lvert p \rvert_p = p^{-1}$ |

## Further Reading

- John Tate, *Rigid analytic spaces* (Inventiones Mathematicae 12, 1971), for the Tate algebra, the acyclicity theorem and the foundations.
- Siegfried Bosch, Ulrich Güntzer and Reinhold Remmert, *Non-Archimedean Analysis* (Springer, 1984), for the systematic theory of affinoid algebras and the maximum modulus principle.
- Jean Fresnel and Marius van der Put, *Rigid Analytic Geometry and its Applications* (Birkhäuser, 2004), for the function theory on affinoid domains and the reduction techniques.
- Hans Grauert and Reinhold Remmert, *Non-Archimedean Analytic Functions* (Springer, 1984), for the Weierstrass division and preparation theorems in the multivariate setting.
- Vladimir G. Berkovich, *Spectral Theory and Analytic Geometry over Non-Archimedean Fields* (American Mathematical Society, 1990), for the comparison between the rigid and the Berkovich points of view.
- Marc Krasner, *Prolongement analytique uniforme et multiforme dans les corps valués complets* (Colloques Internationaux du CNRS, 1963), for the lemma on the analytic continuation of algebraic elements.
- Yvette Amice, *Les nombres $p$-adiques* (Presses Universitaires de France, 1975), for an introductory treatment of the Tate algebra and its norms.
