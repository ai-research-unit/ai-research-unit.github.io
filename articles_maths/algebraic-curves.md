# __Algebraic Curves__

## Introduction

An algebraic curve over a field $K$ is, in the concrete sense of this article, the set of solutions of a polynomial equation in two variables — , better, of a homogeneous polynomial equation in three projective variables — studied through its coordinate ring, its function field, its singular points, its divisors and its rational points. Two features make curves the meeting point of algebra and arithmetic. The first is that a curve is determined, up to birational equivalence, by a field of transcendence degree $1$ over $K$, so that the geometry of curves is the arithmetic of such fields, and every statement about a curve can be read as a statement about a function field and conversely. The second is that the study of the rational points of a curve over a number field or over a finite field is governed by a single invariant, the genus, and by the Riemann–Roch theorem.

This is the *arithmetic* theory of curves. The scheme-theoretic development — schemes, sheaves, coherent cohomology, moduli spaces, stacks — belongs to the Part II agent who owns *Sheaves and Cohomology*, and none of them is used below; the curve is a projective variety of dimension $1$ given by explicit equations, its divisors are formal sums of points, and its class group is the quotient of the divisor group by the principal divisors. The elliptic case, where the genus is $1$ and a rational point makes the curve a group, is *Elliptic Curves*; the function field of a curve over a finite field and its arithmetic are *Global Fields*; the geometry of the plane and of polynomial equations is; the algebra of the coordinate ring is *Rings*, *Unique Factorisation Domains*, *Noetherian and Artinian Rings*, *Integral Extensions and Krull Dimension*, *Dedekind Domains and Ideal Class Groups* and *Valuation Theory and Henselian Rings*; the field-theoretic background is *Field Extensions*, *Splitting Fields and Algebraic Closure*, *Finite Fields* and *Galois Theory*. The local theory of a curve at a place — the completion of the function field, rigid analytic geometry — is Part II's, and is deferred.

Throughout, $K$ is a field, $\bar K$ an algebraic closure, $\mathbb{P}^2$ the projective plane over $\bar K$, $C$ an irreducible curve over $K$, $K(C)$ its function field, $\bar C$ its base change to $\bar K$, and $g$ its genus. A **place** of $K(C)$ is a discrete valuation ring $\mathcal{O}_P$ of $K(C)$ over $K$ with residue field finite over $K$; the places correspond to the points of $\bar C$ in a Galois orbit. The convention of the corpus that the base is the commutative ring, not the field, is not in force here: a curve presupposes a field of definition, and every statement below names the field.

---

## Plane Curves

### Affine and Projective Curves

**Definition.** An **affine plane curve** over $K$ is the zero set in $\mathbb{A}^2(K)$ of a polynomial $f \in K[x,y]$, together with the polynomial; the **coordinate ring** is $K[x,y]/(f)$ and the **function field** $K(C)$ is the fraction field of that ring when $(f)$ is prime. A **projective plane curve** is the zero set in $\mathbb{P}^2$ of a homogeneous $F \in K[x,y,z]$, with coordinate ring the degree-zero part of $K[x,y,z]/(F)$; the affine curve of $f$ is recovered by dehomogenising $F$, and a projective curve is covered by three affine charts.

**Definition.** A curve is **irreducible** if its defining polynomial is irreducible over $\bar K$; **reduced** if the polynomial is squarefree; **geometrically irreducible** if it stays irreducible over $\bar K$. A point $P$ of $C$ is **nonsingular** if not all the partial derivatives of the defining polynomial vanish at $P$; the curve is **nonsingular** (or **smooth**) if every point of $\bar C$ is nonsingular. The **local ring** of $C$ at a nonsingular point is a discrete valuation ring and defines a **place** of $K(C)$, with the coordinate functions having well-defined orders at $P$; if $P$ is defined over $K$, the residue field is $K$ and the place is of degree $1$.

**Theorem (function field).** Let $C$ be an irreducible projective curve over $K$, nonsingular.

**(a)** $K(C)$ is a finitely generated extension of $K$ of transcendence degree $1$, and $K$ is the field of constants, that is, the algebraic closure of $K$ in $K(C)$ is $K$, exactly when $C$ is geometrically irreducible.

**(b)** Every $K$-algebra of finite type which is a domain of Krull dimension $1$ with field of fractions $K(C)$ and which is integrally closed in $K(C)$ is the coordinate ring of an affine model of $C$; the model of $C$ over $K$ is determined by $K(C)$ up to isomorphism.

**(c)** Two nonsingular projective curves over $K$ are isomorphic over $K$ if and only if their function fields are isomorphic over $K$; two irreducible curves are **birationally equivalent** if their function fields are isomorphic.

**Proof sketch.** (a) is the theory of transcendence degree from *Field Extensions*; (b) is the theory of integrally closed domains of dimension $1$ from *Dedekind Domains and Ideal Class Groups* and *Integral Extensions and Krull Dimension*, applied to the coordinate ring; (c) is proved by reading off the points as the discrete valuation rings of $K(C)$ — the valuative dictionary, which is the content of *Valuation Theory and Henselian Rings* — and recovering the projective curve by comparing the coordinate rings of its affine models. $\square$

**Example.** For the line $y = x$ the function field is $K(t)$ with $t = x$; for the conic $y^2 = x^2-1$ the function field is $K(\sqrt{x^2-1})$ with $x = t$; the two are not isomorphic over $K$, but over $K(i)$ the second becomes rational after the substitution $x = (u^2+1)/(2u)$, $y = (u^2-1)/(2u)$ and the curve is birational to the line. A curve birational to the line is called **rational**, and a nonsingular projective curve rational over $K$ has $K(C) \cong K(t)$, hence genus $0$.

### Bezout's Theorem

**Definition.** Let $C$ and $D$ be plane curves over $\bar K$ of degrees $m$ and $n$ with no common component, and $P \in C \cap D$. The **intersection multiplicity** $I_P(C,D)$ is the dimension over $\bar K$ of the local ring of the plane at $P$ localised at the ideal $(C,D)$, or equivalently the length of that ring as a module over itself; it is a nonnegative integer, positive exactly when $P \in C \cap D$. If $C$ and $D$ meet **transversally** at $P$, that is, with distinct tangents at a nonsingular point of each, then $I_P(C,D) = 1$.

**Theorem (Bézout).** Let $C, D$ be projective plane curves over $\bar K$ of degrees $m, n$ with no common component. Then

$$
\sum_{P \in C \cap D} I_P(C,D) = mn .
$$

**Proof sketch.** The intersection number is the degree of the resultant of the two defining forms with respect to one of the variables, and the resultant is a form of degree $mn$; the localised multiplicities are exactly the multiplicities of its roots. This is the classical pro, and it is made rigorous by the theory of resultants, whose algorithm is the elimination. $\square$

**Corollary.** Two lines of $\mathbb{P}^2$ meet in exactly one point; a line and a conic meet in two points counted with multiplicity; two conics meet in four points counted with multiplicity — in each case a statement about the number of solutions of a system of polynomial equations in the projective plane.

**Example.** The conics $x^2 = yz$ and $y^2 = xz$ over $\mathbb{C}$ meet at $(0,0,1)$, $(1,1,1)$, $(\omega,\omega^2,1)$ and $(\omega^2,\omega,1)$ for $\omega$ a primitive cube root of unity — four points, each of intersection multiplicity $1$, and $mn = 4$. The conics $y^2 = xz$ and $y^2 = xz+z^2$ over $\mathbb{C}$ meet only where $z = 0$ and $y = 0$, that is, at the single point $(1,0,0)$, and since $mn = 4$ the intersection multiplicity there is $4 = 2\cdot2$: the two conics are tangent to order $4$ at their common point at infinity.

### The Genus of a Plane Curve

**Definition.** The **arithmetic genus** of a plane curve $C$ of degree $d$ with no multiple components is $p_a(C) = \frac{(d-1)(d-2)}{2}$, and the **geometric genus** of an irreducible curve is $g = \dim_{\bar K} H^0(\bar C,\Omega^1)$ — the dimension of the space of regular differentials, a purely algebraic invariant of the function field defined as the dimension of the vector space of differential forms $\sum f_i\,\mathrm{d}x_i$ regular at every place. For a nonsingular projective curve the two agree, $g = p_a$, and for a singular curve $g = p_a - \sum_P \delta_P$ where $\delta_P \geq 1$ is the **delta invariant** of the singularity.

**Theorem (genus of a nonsingular plane curve).** Let $C \subset \mathbb{P}^2$ be an irreducible nonsingular curve of degree $d$. Then

$$
g = \frac{(d-1)(d-2)}{2} .
$$

**Proof sketch.** One counts the dimension of the space of degree-$m$ forms modulo the multiples of the defining form of degree $d$, using that the restriction to a nonsingular curve is surjective and the adjunction computation below. The regular differentials are the forms $A\,\Omega/F$ with $A$ a form of degree $d-3$ and $\Omega$ the standard $3$-form $x\,\mathrm{d}y\wedge\mathrm{d}z - y\,\mathrm{d}x\wedge\mathrm{d}z + z\,\mathrm{d}x\wedge\mathrm{d}y$, and this space has dimension $\binom{d-1}{2} = (d-1)(d-2)/2$. $\square$

**Example.** $d = 1$: a line, $g = 0$. $d = 2$: a conic, $g = 0$. $d = 3$: a plane cubic, $g = 1$ — the elliptic curves of *Elliptic Curves*, in their Weierstrass and Legendre forms. $d = 4$: $g = 3$, the plane quartic. The Fermat curve $x^d+y^d+z^d = 0$ for $d$ prime to the characteristic is nonsingular of degree $d$, hence has genus $(d-1)(d-2)/2$: genus $0$ for $d = 1,2$, genus $1$ for $d = 3$, genus $3$ for $d = 4$, genus $6$ for $d = 5$.

**Example.** The nodal cubic $y^2z = x^3$ has degree $3$, so $p_a = 1$, and its unique singularity is the node at $(0:0:1)$ with delta invariant $\delta = 1$, so $g = 0$: the curve is rational, with the parametrisation $(x,y,z) = (t^2:t^3:1)$, since $y^2 = t^6 = (t^2)^3 = x^3$ in the chart $z = 1$. The normalisation of the curve is the projective line.

---

## Divisors and Linear Systems

**Definition.** A **divisor** on a nonsingular projective curve $C$ over $K$ is a finite formal sum $D = \sum_{P} n_P P$ of points of $\bar C$ with integral coefficients, invariant under $\operatorname{Gal}(\bar K/K)$, and the **degree** is $\deg D = \sum n_P[K(P):K]$, the sum of the coefficients weighted by the degree of the point. The **principal divisor** of a rational function $f \in K(C)^\times$ is

$$
\operatorname{div}(f) = \sum_P v_P(f) P,
$$

where $v_P$ is the order of vanishing at the place $P$ of the discrete valuation ring of functions regular at $P$; a principal divisor has degree $0$ by the product formula of *Global Fields*. Two divisors are **linearly equivalent**, written $D \sim D'$, if $D - D' = \operatorname{div}(f)$ for some $f \in K(C)^\times$.

**Definition.** The **divisor class group** (also **Picard group**) of degree zero is $\operatorname{Pic}^0(C) = \operatorname{Div}^0(C)/\{\operatorname{div}(f)\}$. Over a finite field it is finite, of order $h_C$ the **class number** of the curve, as in *Global Fields*; for $C = \mathbb{P}^1$ it is trivial, and for a curve of genus $1$ with a rational point it is the group of that point, by the identification of the previous example. The **space of functions with poles bounded by $D$** is

$$
L(D) = \{f \in K(C)^\times : \operatorname{div}(f) + D \geq 0\} \cup \{0\},
$$

a $K$-vector space of finite dimension $\ell(D)$.

**Theorem (Riemann–Roch, stated).** Let $C$ be a nonsingular projective curve of genus $g$ over $K$ and $K_C$ a **canonical divisor**, that is, the divisor of any nonzero rational differential form on $C$. Then

$$
\ell(D) - \ell(K_C - D) = \deg D + 1 - g ,
$$

$\deg K_C = 2g - 2$, and $g = \ell(K_C)$. The theorem and its pro, together with the duality statement for the space of differentials, are not covered here.

**Example.** For $C = \mathbb{P}^1$: $g = 0$, $K_C = -2P$ for any point $P$, and $\ell(D) = \deg D + 1$ for $\deg D \geq 0$; hence every divisor of degree $0$ on the line is principal, so $\operatorname{Pic}^0(\mathbb{P}^1) = 0$ and the class number is $1$. A divisor of degree $d$ on $\mathbb{P}^1$ is the divisor of zeros and poles of a rational function of degree $d$ when $\ell(D) = d+1$, exactly as the classical theory of rational functions requires.

**Example.** For a nonsingular cubic $C$ over $K$ with a rational point $O$, the Riemann–Roch theorem gives $\ell(D) - \ell(K_C-D) = \deg D$ for $\deg K_C = 0$ with $K_C = 0$; for $\deg D = 1$ one gets $\ell(D) = 1$ when $\deg D > 0$, and the map $P \mapsto$ the class of $P - O$ identifies the points with the divisor classes of degree $0$; the group law of *Elliptic Curves* is exactly this identification, and $\operatorname{Pic}^0(C)$ is the group $E(K)$ when $K$ is the field of definition.

---

## Curves over Finite Fields

### The Zeta Function and the Weil Bound

**Theorem (Weil bound).** Let $C$ be a geometrically irreducible nonsingular projective curve of genus $g$ over $\mathbb{F}_q$. Then

$$
\lvert \lvert C(\mathbb{F}_q)\rvert - (q+1)\rvert \leq 2g\sqrt q ,
$$

and more precisely, the **zeta function** of $C$,

$$
Z(C,T) = \exp\left(\sum_{n \geq 1}\lvert C(\mathbb{F}_{q^n})\rvert \frac{T^n}{n}\right) = \frac{P(T)}{(1-T)(1-qT)},
$$

has $P \in \mathbb{Z}[T]$ of degree $2g$ with $P(T) = \prod_{i=1}^{2g}(1-\alpha_iT)$ and $\lvert \alpha_i\rvert = \sqrt q$ for every $i$; the last statement is the Riemann hypothesis for curves, proved by Weil. The exponential is the formal one and the identity is of formal power series, so no convergence is involved; the values $\lvert \alpha_i\rvert = \sqrt q$ are real numbers and their appearance is the only analytic ingredient.

**Proof sketch.** The functional equation $Z(C,1/qT) = q^{1-g}T^{2-2g}Z(C,T)$ and the rationality are proved by the Riemann–Roch theorem and the geometry of the Jacobian; the absolute values of the $\alpha_i$ follow from the positivity of the intersection numbers of divisors on the surface $C\times C$, and the full proof, which belongs to the intersection theory of the Part II agent's algebraic geometry, is deferred. That the bound implies $\lvert C(\mathbb{F}_q)\rvert$ grows like $q$ is the arithmetic content, and it gives $\lvert C(\mathbb{F}_q)\rvert > 0$ for $q$ large. $\square$

**Example.** For $g = 0$: a nonsingular conic over $\mathbb{F}_q$ has exactly $q+1$ points, so the bound is attained; the projective line is the model. For $g = 1$: the bound reads $\lvert \lvert E(\mathbb{F}_q)\rvert-(q+1)\rvert \leq 2\sqrt q$, which is Hasse's theorem of *Elliptic Curves*, and the zeta function is the one computed there. For $q = 2$, $g = 1$: the point count is $2+1+a$ with $\lvert a\rvert \leq 2\sqrt2 \approx 2.83$, so $a \in \{-2,-1,0,1,2\}$ and the count is one of $1,2,3,4,5$; the curve $y^2+y = x^3+x$ over $\mathbb{F}_2$ has the points $O$, $(0,0)$, $(0,1)$, $(1,0)$, $(1,1)$ — five points, so $a = 2$, the largest value allowed by the inequality.

**Example (a curve attaining the bound).** For $q$ a prime power, the **Hermitian curve**

$$
H_q : y^q + y = x^{q+1}
$$

over $\mathbb{F}_{q^2}$ is nonsingular of genus $g = q(q-1)/2$ and has exactly $q^3+1$ rational points over $\mathbb{F}_{q^2}$. The Weil bound gives

$$
q^2+1 + 2gq = q^2 + 1 + q^2(q-1) = q^3+1 ,
$$

so the curve attains the bound; for $q = 2$ this is the curve $y^2+y = x^3$ over $\mathbb{F}_4$, of genus $1$ and with $9$ points, and for $q = 3$ the curve $y^3+y = x^4$ over $\mathbb{F}_9$, of genus $3$ and with $28$ points, against the bound $9+1+2\cdot3\cdot3 = 28$.

### Rational Points and the Local–Global Principle

**Theorem (rational points on conics).** Let $C$ be a nonsingular conic over a field $K$. Then $C$ is rational over $K$ — that is, $C(K) \neq \emptyset$ and $C \cong \mathbb{P}^1$ over $K$ — if and only if $C(K) \neq \emptyset$; and over a finite field $K = \mathbb{F}_q$ every nonsingular conic has a rational point, hence $q+1$ of them.

**Proof sketch.** For the first statement, projection from a rational point $P$ of the conic onto a line gives an explicit birational parametrisation with coefficients in $K$, invertible by the inverse of the projection. For the second, the count of points of a nonsingular conic over $\mathbb{F}_q$ is $q+1$ by the Weil bound for $g = 0$, and this count is positive. $\square$

**Theorem (Hasse principle for conics, statement).** Let $C$ be a nonsingular conic over $\mathbb{Q}$. Then $C(\mathbb{Q}) \neq \emptyset$ if and only if $C(\mathbb{R}) \neq \emptyset$ and $C(\mathbb{Q}_p) \neq \emptyset$ for every prime $p$. The fields $\mathbb{Q}_p$ are the completions of $\mathbb{Q}$, which are constructed and in Part II; the theorem is recorded here for completeness, and its proof and its uses belong to the place where those fields exist.

**Example.** The conic $x^2+y^2+z^2 = 0$ has no rational point, so it is not rational over $\mathbb{Q}$; over $\mathbb{R}$ it has no point either, and it is the failure at the real place that the Hasse principle detects. The conic $x^2+y^2 = 3z^2$ has no rational point although it has real points and points over every $\mathbb{Q}_p$ except one, and this is the classical counterexample showing that the Hasse principle for conics is a genuine theorem rather than a triviality. The example is stated, not proved, since the $\mathbb{Q}_p$ are not available in this Part.

### The Arithmetic of a General Curve

**Theorem (points and the genus).** Let $C$ be a geometrically irreducible nonsingular projective curve of genus $g$ over a field $K$.

**(a)** If $K$ is algebraically closed, the rational points are the points of $\bar C$, and $C$ is rational exactly when $g = 0$; a curve of genus $g \geq 1$ is not rational and, when $K$ is a number field and $g \geq 2$, the set $C(K)$ is finite — the theorem of Faltings, whose proof uses the moduli of curves and is therefore outside this Part.

**(b)** If $K$ is a finite field, $\lvert C(\mathbb{F}_q)\rvert \geq q+1-2g\sqrt q$ by the Weil bound, so $C$ has rational points as soon as $q+1 > 2g\sqrt q$; for small $q$ and large $g$ this leaves open the possibility of a curve without rational points, and the question of the exact minimum number of points of a curve of genus $g$ over $\mathbb{F}_q$ is a subject in its own right.

**(c)** For the function field $K(C)$ of a curve over a finite field the arithmetic of divisors, class numbers, places and the reciprocity law is exactly the theory of *Global Fields*; the class number of a curve of genus $g$ with $q+1$ or more rational points is bounded by the number of points, and its computation is the arithmetic of the Jacobian, whose theory belongs to the Part where abelian varieties are available.

**Example.** For $g = 0$ over $\mathbb{F}_2$: the conic has $3$ points, and $(q+1) - 2g\sqrt q = 3$, so the bound is exact. For $g = 1$ over $\mathbb{F}_2$: the bound reads $3 - 2\sqrt2 \approx 0.17$, so a curve of genus $1$ over $\mathbb{F}_2$ has at least one rational point; the curve $y^2+y = x^3+x$ has five, as computed above. For $g = 2$ over $\mathbb{F}_2$: $3-4\sqrt2 \approx -2.66$, so the bound is vacuous and says nothing; the exact minimum number of rational points of a genus-$2$ curve over $\mathbb{F}_2$ requires a separate analysis of the possible zeta functions rather than the bound.

---

## Summary

An algebraic curve over a field $K$ is studied through its defining polynomial, its coordinate ring, its function field $K(C)$ and its places. The function field is a finitely generated extension of transcendence degree $1$, the places are the discrete valuation rings of $K(C)$ over $K$, and two nonsingular projective curves are isomorphic exactly when their function fields are; the dictionary between the curve and the field is the reason geometry and arithmetic coincide here. Bézout's theorem gives $\sum_P I_P(C,D) = mn$ for plane curves of degrees $m$ and $n$ without common components, and a nonsingular plane curve of degree $d$ has genus $(d-1)(d-2)/2$; singularities lower the genus by the delta invariants, so the nodal cubic has genus $0$ and is rational.

Divisors, principal divisors and linear equivalence give the group $\operatorname{Pic}^0(C)$, and the Riemann–Roch theorem $\ell(D)-\ell(K_C-D) = \deg D+1-g$ — stated here, developed — governs the dimension of the space of functions with bounded poles; for $\mathbb{P}^1$ it shows that every degree-zero divisor is principal, and for a cubic with a rational point it reproduces the group law of *Elliptic Curves*.

Over a finite field the zeta function of a curve is a rational function $P(T)/((1-T)(1-qT))$ with $P$ of degree $2g$, whose analytic theory and whose Riemann hypothesis belong to Part III; the Weil bound $\lvert \lvert C(\mathbb{F}_q)\rvert-(q+1)\rvert \leq 2g\sqrt q$ governs the number of rational points; a conic has exactly $q+1$ points, an elliptic curve obeys Hasse's bound, and the Hermitian curve $y^q+y = x^{q+1}$ over $\mathbb{F}_{q^2}$ of genus $q(q-1)/2$ attains the bound with $q^3+1$ points. A nonsingular conic is rational over $K$ exactly when it has a $K$-rational point, and the Hasse principle for conics over $\mathbb{Q}$ is stated with its local formulation deferred to Part II, where the completions exist. The scheme-theoretic language, sheaf cohomology, the moduli of curves and the proofs of the Weil conjectures in higher dimension belong to Part II and to the algebraic-geometry agent, and are not used here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$, $\bar K$ | Base field, algebraic closure |
| $\mathbb{A}^2$, $\mathbb{P}^2$ | Affine and projective planes |
| $C$, $D$ | Curves |
| $K(C)$ | Function field of $C$ |
| $P$, $[K(P):K]$ | Point, degree of a point |
| $I_P(C,D)$ | Intersection multiplicity at $P$ |
| $m$, $n$, $d$ | Degrees of plane curves |
| $p_a(C)$ | Arithmetic genus $(d-1)(d-2)/2$ |
| $g$ | Geometric genus |
| $\delta_P$ | Delta invariant of the singularity at $P$ |
| $\operatorname{div}(f)$ | Principal divisor of $f$ |
| $v_P$ | Order of vanishing at $P$ |
| $\operatorname{Div}^0(C)$, $\operatorname{Pic}^0(C)$ | Degree-zero divisors, divisor class group |
| $L(D)$, $\ell(D)$ | Space of functions with poles bounded by $D$, its dimension |
| $K_C$ | Canonical divisor |
| $\lvert C(\mathbb{F}_q)\rvert$ | Number of rational points over $\mathbb{F}_q$ |
| $Z(C,T)$ | Zeta function of $C$ |
| $\alpha_i$ | Reciprocal roots of $P(T)$, of absolute value $\sqrt q$ |
| $H_q$ | Hermitian curve $y^q+y = x^{q+1}$ over $\mathbb{F}_{q^2}$ |





## Further Reading

- William Fulton, *Algebraic Curves: An Introduction to Algebraic Geometry* (Benjamin, 1969), for the elementary treatment of plane curves, Bézout's theorem, divisors and Riemann–Roch.
- Robert J. Walker, *Algebraic Curves* (Princeton University Press, 1950), for the classical projective and intersection-theoretic development.
- André Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent* (Hermann, 1948), for the Riemann hypothesis for curves and the bound on the number of rational points.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the places and completions of the function field of a curve.
- Henning Stichtenoth, *Algebraic Function Fields and Codes* (Springer, 2nd ed. 2009), for the function-field formulation of curves, divisors and the zeta function, and for the Hermitian curve.
- Carlos Moreno, *Algebraic Curves over Finite Fields* (Cambridge University Press, 1991), for the arithmetic over finite fields, including the Weil bound and the families of curves attaining it.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the scheme-theoretic development to which this article deliberately defers.
- Gerd Faltings, "Endlichkeitssätze für abelsche Varietäten über Zahlkörpern", *Inventiones Mathematicae* 73 (1983), 349–366, for the finiteness of the rational points of a curve of genus at least $2$ over a number field.
