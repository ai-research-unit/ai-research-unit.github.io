# __The Riemann–Roch Theorem for Curves__

## Introduction

The Riemann–Roch theorem is the computation of the dimension of the space of rational functions on a curve with poles bounded by a prescribed divisor. Written

$$
\ell(D) - \ell(K_C - D) = \deg D + 1 - g ,
$$

it relates three quantities: the dimension $\ell(D)$ of the space $L(D)$ of functions whose poles are bounded by $D$, the dimension of the dual space of functions whose poles are bounded by the canonical divisor shifted by $-D$, and the integer $\deg D + 1 - g$ built from the degree of $D$ and the genus $g$ of the curve. Its power is that it converts a question about functions into a question about two integers, and that it is a theorem of pure algebra: $g$, the divisor $D$, the space $L(D)$ and the canonical divisor are all defined over an arbitrary field of definition, no ordering, no distance and no analysis entering. Over the complex numbers the theorem was discovered as the solution of a problem of Abelian integrals; in the form below it is a statement about valuation rings, divisors and vector spaces, valid over any field.

This article develops the theorem and its immediate consequences. The curve is a nonsingular projective curve over a field $K$, treated through its function field, its places and its divisors, as in *Algebraic Curves*; the genus is defined as the dimension of the space of regular differentials; the canonical divisor is the divisor of a rational differential form; and the theorem is proved by the standard two-step argument, with the details of the duality stated rather than developed. The scheme-theoretic and cohomological formulation — the identification of the two sides with sheaf cohomology groups — belongs to the Part II agent who owns *Sheaves and Cohomology*, and is not used. The function-field reading, and particularly the function-field form of the product formula used below, is *Global Fields*; the elliptic case is *Elliptic Curves*; the finite-field counting consequences are stated there and in *Algebraic Curves*.

Throughout, $C$ is a nonsingular projective curve over a field $K$, geometrically irreducible unless stated otherwise, $g$ is its genus, $K(C)$ its function field, and for a divisor $D$ on $C$ the space $L(D)$ and its dimension $\ell(D)$ are as in *Algebraic Curves*. The conventions of the corpus hold: the base may be any field, and every statement names the hypothesis on the characteristic that it needs.

---

## Divisors, Differentials and the Genus

### The Space $L(D)$

**Definition.** Let $D = \sum_P n_PP$ be a divisor on $C$ and let $v_P$ be the order of vanishing at the place $P$. The **Riemann–Roch space** is

$$
L(D) = \{f \in K(C)^\times : v_P(f) + n_P \geq 0 \ \text{for every } P\} \cup \{0\},
$$

a $K$-vector space of finite dimension $\ell(D)$; it is the space of functions whose poles are bounded by $D$. The **index of speciality** of $D$ is $i(D) = \ell(K_C - D)$, where $K_C$ is the canonical divisor defined below, and $D$ is **special** if $i(D) > 0$, that is, if $\ell(D)$ exceeds the value forced by Riemann's inequality.

**Theorem.** Let $D, D'$ be divisors on $C$.

**(a)** $L(D)$ is finite-dimensional over $K$ and $\ell(D) = 0$ for $\deg D < 0$; if $D \leq D'$ then $L(D) \subseteq L(D')$.

**(b)** $L(D) \cong L(D')$ as $K$-vector spaces whenever $D \sim D'$, via multiplication by the function relating them; in particular $\ell(D)$ depends only on the linear equivalence class of $D$.

**(c)** $\ell(D) \leq \deg D + 1$ whenever $\deg D \geq 0$.

**Proof.** (a) A function whose poles are bounded by $D$ is determined by its expansion at the places in the support of $D$ up to a bounded number of terms, and there are finitely many such places; the vanishing for $\deg D < 0$ is the degree-zero property of principal divisors. (b) If $D' = D + \operatorname{div}(h)$ then $f \mapsto fh$ is the required isomorphism. (c) is proved by induction on $\deg D$: choose $P$ with $n_P > 0$ and use that $L(D-P) \subseteq L(D)$ with quotient of dimension at most $1$. $\square$

### Differential Forms and the Canonical Divisor

**Definition.** A **rational differential form** on $C$ is an element of the one-dimensional $K(C)$-vector space $\Omega_{K(C)/K}$ of Kähler differentials; in terms of a separating transcendence basis $x$ it is $f\,\mathrm{d}x$ with $f \in K(C)$. For a place $P$ with uniformiser $t_P$ one writes $\omega = g\,\mathrm{d}t_P$ and defines $v_P(\omega) = v_P(g)$, a well-defined integer independent of the choice of $t_P$ up to an invertible factor. The **divisor** of $\omega \neq 0$ is $\operatorname{div}(\omega) = \sum_P v_P(\omega)P$, and the **canonical divisor** $K_C$ is the divisor of any nonzero rational differential form; two such divisors differ by the divisor of a rational function, so $K_C$ is well defined up to linear equivalence. The form is **regular** at $P$ if $v_P(\omega) \geq 0$, and **regular** if this holds at every place; the space of regular forms is denoted $\Omega(C)$.

**Theorem.** Let $C$ be a nonsingular projective curve over $K$.

**(a)** $\Omega(C)$ is a finite-dimensional $K$-vector space, and its dimension is the **genus** $g$ of $C$; equivalently $g = \ell(K_C)$.

**(b)** $\deg K_C = 2g-2$; consequently $\ell(K_C) - \ell(0) = (2g-2)+1-g = g-1$, in agreement with (a).

**(c)** The genus is invariant under extension of the base field: $g(C) = g(C_{\bar K})$.

**Proof sketch.** (a) The space of regular differentials is the space of functions with poles bounded by $K_C$, so $\dim\Omega(C) = \ell(K_C)$ by definition of the divisor of a form; that this dimension is finite follows from the finiteness in the previous theorem. (b) is proved by counting the zeros and poles of a differential form with the degree-zero property of principal divisors, or by the Riemann–Roch theorem below applied at $D = K_C$. (c) The definition of the divisor of a form is stable under base change. $\square$

**Example.** For $C = \mathbb{P}^1$: with the coordinate $x$ the form $\mathrm{d}x$ has a double pole at infinity and no other pole, so $K_{\mathbb{P}^1} = -2P_\infty$ and $\deg K = -2 = 2g-2$, giving $g = 0$; the only regular differentials are multiples of $\mathrm{d}x$ vanishing nowhere, and indeed $\Omega(\mathbb{P}^1) = 0$ since a rational function with no poles is constant and a nonzero constant form is not regular at infinity.

**Example.** For a nonsingular plane curve $C$ of degree $d$: taking the form $\Omega = x\,\mathrm{d}y\wedge\mathrm{d}z - y\,\mathrm{d}x\wedge\mathrm{d}z + z\,\mathrm{d}x\wedge\mathrm{d}y$ restricted to $C$ in the chart where a dehomogenising variable is nonzero shows that $\operatorname{div}(\Omega/F)$ is the divisor of a line section to the power $d-3$; hence

$$
K_C = (d-3)H, \qquad \deg K_C = d(d-3) = 2g-2, \qquad g = \frac{(d-1)(d-2)}{2},
$$

recovering the genus formula of *Algebraic Curves*. For $d = 4$ this gives $g = 3$ and $K_C = H$, a line section of degree $4$; for $d = 3$ it gives $g = 1$ and $K_C = 0$, the canonical divisor of an elliptic curve being trivial.

---

## The Riemann–Roch Theorem

### Statement and the Reduction

**Theorem (Riemann–Roch).** Let $C$ be a nonsingular projective curve of genus $g$ over a field $K$ and $D$ a divisor on $C$. Then

$$
\ell(D) - \ell(K_C-D) = \deg D + 1 - g .
$$

**Theorem (Riemann's inequality).** Under the same hypotheses, $\ell(D) \geq \deg D + 1 - g$; equivalently $\deg D + 1 - \ell(D) \leq g$ for every divisor $D$, so that $g = \max_D\,(\deg D + 1 - \ell(D))$, the maximum being attained at every divisor of degree at least $2g-1$, where the index of speciality vanishes.

**Proof sketch of the theorem.** The argument proceeds in three steps.

*(i) The theorem holds for $D = 0$ and $D = K_C$.* At $D = 0$ one has $\ell(0) = 1$, and $K_C - 0 = K_C$ with $\ell(K_C) = g$, so both sides are $1-g$; at $D = K_C$ the same computation reads $\ell(K_C)-\ell(0) = g-1$.

*(ii) The theorem holds for $\deg D \geq 2g-1$.* For such $D$ one shows $\ell(K_C-D) = 0$ by an argument of Riemann's, using that a nonzero regular differential has no more than $2g-2$ zeros, and then $\ell(D) = \deg D+1-g$ follows from Riemann's existence argument: functions with prescribed principal parts at the places of a divisor of large degree exist subject to exactly $g$ linear conditions. This is the classical representation-theoretic heart of the theorem.

*(iii) The theorem holds for all $D$ by descending induction.* It suffices to show that if the theorem holds for $D+P$ then it holds for $D$. One has $\ell(D+P)-\ell(D) \in \{0,1\}$ and $\ell(K_C-D)-\ell(K_C-D-P) \in \{0,1\}$, since the quotient of two successive Riemann–Roch spaces has dimension at most $1$; and the total $\ell(D)-\ell(K_C-D) - \deg D$ changes by $(\ell(D+P)-\ell(D)) - (\ell(K_C-D)-\ell(K_C-D-P)) - 1$ when passing from $D$ to $D+P$, which is $0$ because the two increments cannot differ, by a residue or trace argument applied to the functions realising them. Granting that step, (ii) descends to all $D$.

The two ingredients that are stated rather than proved here — Riemann's existence argument and the increment comparison — are the content of the duality $L(K_C-D)^\ast \cong \Omega(D)$ between functions with poles bounded by $K_C-D$ and differentials with poles bounded by $-D$, whose sheaf-theoretic formulation is the Serre duality of the Part II agent's *Sheaves and Cohomology*. $\square$

**Corollary (Riemann–Roch, computational form).** For a divisor $D$ of degree $\deg D \geq 2g-1$ one has $\ell(D) = \deg D+1-g$, and for $\deg D < 0$ one has $\ell(D) = 0$. For $0 \leq \deg D \leq 2g-2$ the value of $\ell(D)$ is $\deg D + 1 - g + i(D)$ with $i(D) = \ell(K_C-D) \geq 0$, and $i(D) = 0$ for all divisors of degree $2g-1$ and above.

**Theorem (Clifford).** Let $D$ be a divisor on $C$ with $0 \leq \deg D \leq 2g-2$. Then

$$
\ell(D) \leq \frac{\deg D}{2} + 1 ,
$$

with equality if and only if $D = 0$, or $D \sim K_C$, or $C$ is hyperelliptic and $D$ is linearly equivalent to a multiple of the hyperelliptic pencil of degree $2$.

**Proof.** Applying Riemann–Roch to $D$ and to $K_C-D$ and adding the two inequalities $\ell(D) \geq \deg D+1-g$ and $\ell(K_C-D) \geq \deg(K_C-D)+1-g$ gives the bound; the equality case is a separate analysis of when both inequalities are equalities, and it is the classification of the "half-canonical" divisors. $\square$

**Example.** For $C = \mathbb{P}^1$: $g = 0$, $K_C = -2P_\infty$, and Riemann–Roch reads $\ell(D)-\ell(-2P_\infty-D) = \deg D+1$; for $\deg D \geq -1$ the index vanishes and $\ell(D) = \deg D+1$, so a divisor of degree $d \geq 0$ is the divisor of zeros and poles of a rational function of degree $d$, and $\ell(D) = d+1$ is exactly the dimension of the space of such functions; for $\deg D < 0$ one gets $\ell(D) = 0$ and $\ell(-2P_\infty-D) = -\deg D-1$, consistent with the identification of the dual space.

**Example.** For an elliptic curve $C$ with a rational point $O$ and genus $1$: $K_C = 0$, so Riemann–Roch reads $\ell(D) - \ell(-D) = \deg D$, and for $\deg D > 0$ this gives $\ell(D) = \deg D$. Hence $\ell(nO) = n$ for every $n \geq 1$: taking a basis $1, x$ of $L(2O)$ and adjoining $y \in L(3O)$ with $y \notin L(2O)$, the functions $1, x, y, x^2, xy, x^3, y^2$ all lie in $L(6O)$ of dimension $6$, so they satisfy a linear relation, which is the Weierstrass equation of *Elliptic Curves*. The genus-$1$ curve is therefore a plane cubic, and the group law is the divisor class group, exactly as reconstructed there.

**Example (hyperelliptic curves).** Let $g \geq 2$ and suppose $C$ carries a divisor $D$ of degree $2$ with $\ell(D) = 2$. Then $i(D) = \ell(K_C-D) = 2-(2+1-g) = g-1$, so $D$ is special, and the map to $\mathbb{P}^1$ given by the pencil $L(D)$ has degree $2$: the curve is **hyperelliptic**. Riemann–Roch with $D = K_C - D$ gives $\ell(K_C-D) = g-1$, and Clifford's bound is attained at $D$, so this is exactly the equality case. For $g = 2$ every curve is hyperelliptic, since $K_C$ has degree $2$ and $\ell(K_C) = 2$; for $g = 3$ the hyperelliptic curves are those for which $K_C$ is a multiple of the degree-$2$ pencil, and the non-hyperelliptic ones are the plane quartics.

---

## Consequences and Applications

### Riemann–Hurwitz

**Theorem (Riemann–Hurwitz).** Let $\phi : C \to C'$ be a finite separable morphism of nonsingular projective curves over $K$ of degree $n$, with constant fields $K_C$, $K_{C'}$ and $K'' = C'_{K_{C}}$, so that $[C:K''C'] = n/[K_C:K_{C'}] =: n_0$. Then

$$
2g_C - 2 = n_0(2g_{C'}-2) + \deg \mathfrak{D}_{C/C'},
$$

where $\mathfrak{D}_{C/C'}$ is the different of the extension of function fields, of degree $\sum_{P \in C}(d(P)-1)[K(P):K]$ with $d(P) \geq e(P)-1$ the different exponent at $P$ and $e(P)$ the ramification index.

This is the Riemann–Hurwitz formula of *Global Fields* in the corrected form stated there, where the factor $n_0$ is explained by the constant field extension; the uncorrected form with the full degree $n$ is false for constant field extensions, as the example $C = \mathbb{P}^1_{\mathbb{F}_{q^2}}$, $C' = \mathbb{P}^1_{\mathbb{F}_q}$ shows, where both genera are $0$ and the different is trivial.

**Corollary (the Hurwitz bound).** Let $C$ be a curve of genus $g \geq 2$ over a field of characteristic $0$. Then the group $\operatorname{Aut}(C)$ of automorphisms of $C$ over $K$ is finite and

$$
\lvert \operatorname{Aut}(C)\rvert \leq 84(g-1).
$$

**Proof sketch.** An automorphism of finite order $n > 1$ with quotient $C/\langle\sigma\rangle$ of genus $g_0$ and $r$ branch points gives, by Riemann–Hurwitz, $2g-2 \geq n(2g_0-2)+r(n-1) \geq n(2g_0-2)+n-1$; combining with Riemann–Roch for the quotient map yields the numerical bound $n \leq 84(g-1)$ for a single automorphism, and the full group is bounded by the same argument applied to the whole group acting with its orbit decomposition. $\square$

**Example.** The bound is attained for infinitely many genera; for $g = 3$ it gives $84\cdot2 = 168$, and the Klein quartic $x^3y + y^3z + z^3x = 0$ has $g = 3$ and exactly $168$ automorphisms, so the bound is attained there. In characteristic $p > 0$ the bound fails, since a curve such as $y^p - y = x$ has many automorphisms, and the correct statement is the bound $n \leq 2p/(p-2)\cdot(2g-2)$ for the $p$-part, with wild ramification accounting for the difference.

### Existence of Functions and Points

**Corollary (functions with prescribed poles).** Let $D$ be a divisor with $\deg D \geq g$. Then $\ell(D) \geq 1$; if in addition $\deg D \geq 2g-1$ then $\ell(D) = \deg D+1-g \geq g$, and the evaluation map at a general collection of points is surjective.

**Corollary (gap theorem).** Let $C$ have genus $g \geq 1$ and let $P$ be a point of $C$. An integer $w \geq 1$ is a **gap** at $P$ if $\ell(wP) = \ell((w-1)P)$, that is, if there is no function with a pole of order exactly $w$ at $P$ and no other pole; there are exactly $g$ gaps $w_1 < w_2 < \cdots < w_g$, they satisfy $w_i \leq 2g-1$, and

$$
\sum_{i=1}^{g} w_i \geq \frac{g(g+1)}{2},
$$

with equality if and only if the gap sequence is $(1,2,\ldots,g)$; the point is a **Weierstrass point** when this fails. The Weierstrass weight of $P$ is $\sum_i w_i - g(g+1)/2$, and the total weight over all points is $(g-1)g(g+1)$ for $g \geq 2$; in particular the number of Weierstrass points of a curve of genus $g \geq 2$ is at least $2g+2$, with equality for the hyperelliptic curves, whose branch points are exactly the Weierstrass points.

**Proof sketch.** Riemann–Roch gives $\ell(wP) = w+1-g$ as soon as $w \geq 2g-1$, because the index of speciality vanishes there; hence the dimensions $\ell(wP)$ for $1 \leq w \leq 2g-1$ increase from $1$ to $g$ in exactly $2g-1-g = g-1$ steps, leaving exactly $g$ values of $w$ where the dimension does not increase, and these are the gaps. The sum bound follows by adding the $g$ inequalities $w_i \geq i$ modulo the definition of the gaps, and the total-weight formula is the theorem of Hurwitz on the Weierstrass points, proved by counting the zeros of the Wronskian determinant of a basis of $\Omega(C)$. $\square$

**Example.** For $g = 1$ the unique gap at every point is $1$, with $\sum w_i = 1 = g(g+1)/2$: the point is not a Weierstrass point, and indeed $\ell(2P) = 2$ and $\ell(3P) = 3$ give the functions $x$ and $y$ of the Weierstrass equation. For $g = 2$: at the six branch points of the degree-$2$ map, $\ell(2P) = 2$ so that $2$ is not a gap, and $\ell(3P) = 2$ so that $3$ is one, giving gaps $1,3$ and weight $4-3 = 1$; at every other point $\ell(2Q) = 1$ and $\ell(3Q) = 2$, giving gaps $1,2$ and weight $0$. The total weight is $6 = (g-1)g(g+1) = 6$, and the number of Weierstrass points is the minimum $2g+2 = 6$, as it must be for a hyperelliptic curve. For $g = 3$: the plane quartics are not hyperelliptic, and their Weierstrass points have gaps $(1,2,4)$, of weight $1$ each; the total weight is $(g-1)g(g+1) = 24$, so there are exactly $24$ Weierstrass points, the maximum for genus $3$.

**Theorem (Weil bound, restated).** Let $C$ be a geometrically irreducible nonsingular curve of genus $g$ over $\mathbb{F}_q$. Then $\lvert \lvert C(\mathbb{F}_q)\rvert - (q+1)\rvert \leq 2g\sqrt q$, and the zeta function of $C$ satisfies the functional equation and the Riemann hypothesis as stated in *Algebraic Curves*. Riemann–Roch enters through the dimension of the space of functions with bounded poles: it computes $\ell(D)$ for every divisor of degree at least $2g-1$, which controls the number of effective divisors in a linear equivalence class and hence the point counts over all finite extensions.

**Example (adjunction for plane curves).** Let $C$ be a nonsingular plane curve of degree $d$ over a field $K$, so that $g = (d-1)(d-2)/2$. A line section $H$ is a divisor of degree $d$, and the canonical divisor is $K_C = (d-3)H$, of degree $d(d-3) = 2g-2$. Riemann–Roch then reads $\ell(D)-\ell(K_C-D) = \deg D+1-g$, and at $D = K_C$ it gives $\ell(K_C) = g$; at $D = H$ it gives $\ell(H) = 3$ for $d \geq 2$, the three-dimensional space of linear forms on the plane. The same computation with $D = nO$ on a curve of genus $1$ gives $\ell(nO) = n$ for $n \geq 1$, which produces the functions $x$ and $y$ of a Weierstrass equation and so ties the theorem to *Elliptic Curves*. The coding-theoretic use of the spaces $L(G)$, in which the functions with poles bounded by $G$ are evaluated at rational points, belongs.

---

## Summary

For a nonsingular projective curve $C$ over a field $K$, a divisor $D$ of degree $\deg D$ and the canonical divisor $K_C$ of a rational differential form, the Riemann–Roch theorem states $\ell(D)-\ell(K_C-D) = \deg D+1-g$, where $\ell(D)$ is the dimension of the space of functions with poles bounded by $D$ and $g$ is the genus, defined independently as the dimension of the space of regular differentials. Riemann's inequality $\ell(D) \geq \deg D+1-g$ is the weaker form; the index of speciality $i(D) = \ell(K_C-D)$ vanishes for $\deg D \geq 2g-1$, so the dimension is computable from the degree alone in that range; and Clifford's theorem bounds $\ell(D)$ by $\deg D/2+1$ in the special range.

The genus is read off as $\ell(K_C)$, the degree of the canonical divisor is $2g-2$, and for a nonsingular plane curve of degree $d$ the canonical divisor is $(d-3)$ times a line section, so that $\deg K_C = d(d-3)$ and $g = (d-1)(d-2)/2$. Riemann–Roch at the divisor $nO$ on an elliptic curve gives $\ell(nO) = n$, which produces the functions $x$ and $y$ satisfying a Weierstrass equation, so that every genus-$1$ curve with a rational point is a plane cubic; at the degree-$2$ divisor of a hyperelliptic curve it exhibits the degree-$2$ map to the line, and by Clifford's equality case these are exactly the curves carrying such a divisor. The Riemann–Hurwitz formula $2g_C-2 = n_0(2g_{C'}-2)+\deg\mathfrak{D}_{C/C'}$, in the form corrected for constant field extensions in *Global Fields*, computes the genus of an extension from its ramification, and yields the Hurwitz bound $\lvert \operatorname{Aut}(C)\rvert \leq 84(g-1)$ in characteristic $0$, attained by the Klein quartic in genus $3$.

The gap theorem at a point $P$ produces $g$ integers $w_i \leq 2g-1$ with $\sum w_i = g(g+1)/2$, and the Weierstrass points are those whose gap sequence differs from $1,2,\ldots,g$; a plane quartic has $24$ of them, the general upper bound $(g-1)g(g+1)$ being attained there. Over a finite field the theorem controls the point counts of the Weil bound, and over a finite field with a supply of rational points it produces the linear codes, by evaluating functions of $L(G)$ at the rational points. The sheaf-theoretic formulation of the duality used in the pro, and the complete cohomological pro, belong to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C$, $C'$ | Nonsingular projective curves |
| $K$ | Field of definition |
| $K(C)$ | Function field |
| $g$ | Genus, the dimension of the space of regular differentials |
| $D$, $D'$ | Divisors |
| $P$ | A place (point) of $C$ |
| $v_P(f)$ | Order of vanishing of $f$ at $P$ |
| $L(D)$, $\ell(D)$ | Riemann–Roch space, its dimension |
| $i(D)$ | Index of speciality $\ell(K_C-D)$ |
| $K_C$ | Canonical divisor |
| $\Omega(C)$ | Space of regular differential forms |
| $\omega$, $\operatorname{div}(\omega)$ | Rational differential form, its divisor |
| $\mathfrak{D}_{C/C'}$ | Different of a morphism of curves |
| $e(P)$, $d(P)$ | Ramification index, different exponent |
| $H$ | A line section, for a plane curve |
| $w_1,\ldots,w_g$ | Gap sequence at a point |
| $\operatorname{Aut}(C)$ | Automorphism group of $C$ |



## Further Reading

- Bernhard Riemann, "Theorie der Abel'schen Functionen", *Journal für die reine und angewandte Mathematik* 54 (1857), 115–155, for the inequality and the existence argument.
- Gustav Roch, "Über die Anzahl der willkürlichen Constanten in algebraischen Functionen", *Journal für die reine und angewandte Mathematik* 64 (1865), 372–376, for the completion of the theorem.
- William Fulton, *Algebraic Curves: An Introduction to Algebraic Geometry* (Benjamin, 1969), for the elementary proof of Riemann–Roch by the reduction given here.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for Serre duality and the cohomological formulation.
- Max Noether, "Über die invariante Darstellung algebraischer Functionen", *Mathematische Annalen* 17 (1880), 263–284, for the adjunction computation of the canonical divisor of a plane curve.
- Adolf Hurwitz, "Über algebraische Gebilde mit eindeutigen Transformationen in sich", *Mathematische Annalen* 41 (1893), 403–442, for the automorphism bound and the genus computation.
- Karl Weierstrass, "Über das sogenannte Dirichlet'sche Princip", *Mathematische Werke* II (1885), 49–54, for the gap theorem at a point.
- Henning Stichtenoth, *Algebraic Function Fields and Codes* (Springer, 2nd ed. 2009), for the function-field proof of Riemann–Roch and the construction of codes from curves.
