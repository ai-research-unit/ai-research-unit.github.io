# __Elliptic Curves__

## Introduction

An elliptic curve over a field $K$ is a nonsingular projective curve of genus $1$ equipped with a rational point. Equivalently, and more usefully for computation, it is the projective plane curve given by a Weierstrass equation

$$
y^2 + a_1xy + a_3y = x^3 + a_2x^2 + a_4x + a_6, \qquad a_i \in K,
$$

nonsingular at every point. What makes the object central in arithmetic is that its points form an abelian group by a purely geometric construction — the chord–tangent law — so that an elliptic curve carries both a geometric and an algebraic structure, and the two interact: the group law is defined by rational functions with coefficients in $K$, the endomorphisms of the curve are ring endomorphisms of the group, and over a finite field the Frobenius endomorphism is an algebraic integer whose trace determines the number of points.

This is the *arithmetic* theory of curves over a field. The curve is treated concretely, through its Weierstrass equation, its group law, its torsion, its isogenies and its reduction at a prime; the words scheme, sheaf, cohomology, moduli space and stack do not occur, and the corresponding geometric development belongs to the Part II agent who owns *Sheaves and Cohomology*. The analogues for a general curve are andbeing; the arithmetic of the base field is in *Algebraic Number Theory*, *Global Fields* and *Class Field Theory*; the finite-field side uses *Finite Fields*; the abstract theory of extensions uses *Galois Theory*, *Field Extensions* and *Splitting Fields and Algebraic Closure*. Heights, local fields, the reduction theory at a complete base field, the $p$-adic Tate module as a module over the completion, and the $L$-function belong to later Parts, because the logarithm, the absolute value and the completion are not available here; where such a statement is needed it is named and deferred.

Throughout, $K$ is a field, $\bar K$ an algebraic closure, $E$ an elliptic curve over $K$ given by a Weierstrass equation, $O$ the point at infinity, and $E(K)$ the group of $K$-rational points. The characteristic of $K$ is denoted $p$ when it is positive, and a statement needing $\operatorname{char} K \notin \{2,3\}$ says so.

---

## Weierstrass Equations

### Definitions and Invariants

**Definition.** An **elliptic curve** over $K$ is a pair $(E, O)$ where $E$ is a nonsingular projective curve of genus $1$ over $K$ and $O \in E(K)$ is a $K$-rational point. By the Riemann–Roch theorem, the space of functions on $E$ with a pole of order at most $2$ at $O$ and no other poles is two-dimensional, and choosing a basis $1, x$ and then a function $y$ with a pole of order $3$ at $O$ embedding the curve into the projective plane gives a Weierstrass equation as displayed in the introduction; conversely every nonsingular Weierstrass equation defines a curve of genus $1$ with the point $O$ at infinity.

**Definition.** For a Weierstrass equation with $a_i \in K$ one defines, in the general case,

$$
b_2 = a_1^2 + 4a_2, \quad b_4 = 2a_4 + a_1a_3, \quad b_6 = a_3^2 + 4a_6, \quad b_8 = a_1^2a_6 + 4a_2a_6 - a_1a_3a_4 + a_2a_3^2 - a_4^2,
$$

$$
\Delta = -b_2^2b_8 - 8b_4^3 - 27b_6^2 + 9b_2b_4b_6, \qquad c_4 = b_2^2 - 24b_4, \qquad j = c_4^3/\Delta .
$$

The curve is nonsingular if and only if $\Delta \neq 0$; $\Delta$ is the **discriminant** and $j$ the **$j$-invariant** of the equation. For the **short Weierstrass form** $y^2 = x^3 + ax + b$, valid when $\operatorname{char} K \neq 2,3$, these read

$$
\Delta = -16(4a^3 + 27b^2), \qquad c_4 = -48a, \qquad j = 1728\,\frac{4a^3}{4a^3+27b^2} .
$$

For the **Legendre form** $y^2 = x(x-1)(x-\lambda)$ with $\lambda \notin \{0,1\}$, valid when $\operatorname{char} K \neq 2$, one has $\Delta = 16\lambda^2(\lambda-1)^2$ and $j = 2^8\frac{(\lambda^2-\lambda+1)^3}{\lambda^2(\lambda-1)^2}$.

**Example.** For $E: y^2 = x^3 - x$ one has $a = -1$, $b = 0$, so $\Delta = -16(4(-1)^3) = 64 \neq 0$ and $j = 1728\cdot(-4)/(-4) = 1728$. For $E: y^2 = x^3 + 1$ one has $a = 0$, $b = 1$, so $\Delta = -16\cdot27 = -432$ and $j = 0$. For $y^2 = x^3 - 2$ one has $\Delta = -16\cdot27\cdot4 = -1728$ and $j = 0$; the curves $y^2 = x^3 + b$ for varying $b$ all have $j = 0$, and among them the isomorphism classes over an algebraic closure are classified by the sixth powers modulo squares.

**Theorem (admissible changes of variable).** Two Weierstrass equations related by a change of variable

$$
x = u^2x' + r, \qquad y = u^3y' + u^2sx' + t, \qquad u \in K^\times,\ r,s,t \in K,
$$

define isomorphic curves with the same $j$-invariant, and $\Delta$ and $c_4$ transform by $\Delta' = u^{12}\Delta$, $c_4' = u^4c_4$. Conversely, over an algebraically closed field two elliptic curves are isomorphic if and only if their $j$-invariants agree; over a general field, curves with the same $j$-invariant are classified up to isomorphism by the first Galois cohomology of the group $\operatorname{Aut}(E)$, which is finite of order $2$, $4$ or $6$ and acts through automorphisms of the group law, and this classification uses the cohomological language of *Galois Cohomology*.

---

## The Group Law

### The Chord–Tangent Construction

**Theorem (group law).** Let $E$ be an elliptic curve given by a Weierstrass equation, with the point $O$ at infinity.

**(a)** For $P, Q \in E$, let $L$ be the line through $P$ and $Q$, tangent to $E$ at $P$ if $P = Q$, and let $R$ be the third point of $E \cap L$; set $P + Q = -R$, where $-R$ is the reflection of $R$ in the $x$-axis, that is, the unique point whose line with $R$ is the line at infinity together with $R$ — concretely, if $R = (x_R, y_R)$ then $-R = (x_R, -y_R - a_1x_R - a_3)$. Then $E(K)$ is an abelian group with identity $O$ and inverse as just defined.

**(b)** The addition and the inverse are given by rational functions with coefficients in $K$; hence for $P, Q \in E(K)$ one has $P+Q \in E(K)$, and $E(K)$ is an abelian group.

**(c)** The addition is associative, so that $E(K)$ and $E(\bar K)$ are abelian groups; over an algebraically closed field $E(\bar K)$ is divisible by every integer coprime to the characteristic, and over a number field $E(K)$ is finitely generated, by the Mordell–Weil theorem below.

**Proof sketch.** (a) A line meeting $E$ at $P$, $Q$, $R$ has associated function $\ell$ with divisor $P+Q+R-3(O)$, and this divisor is principal exactly because the divisor of a function has degree $0$, by the product formula of *Global Fields*; the rule $P+Q = -R$ says that the three intersection points of a line sum to the identity, which forces $O$ to be the identity and makes the operation a group law, the inverse of $P$ being the third point on the vertical line through $P$ and $O$. (b) Rationality is immediate from the rationality of the coefficients of the chord and of the tangent. (c) Associativity is the Cayley–Bacharach incidence statement for the nine points in which two cubics through eight given points meet: applied to the reducible cubics formed by $E$ together with the three lines defining $(P+Q)+R$ and $P+(Q+R)$, it gives the equality of the two relevant points. $\square$

**Example.** On $E: y^2 = x^3 - x$ over $\mathbb{Q}$, let $P = (1,0)$ and $Q = (-1,0)$. The line through them is $y = 0$, which meets $E$ at $x = -1, 0, 1$; the third point is $R = (0,0)$, so $P + Q = -R = (0,0)$. Consistently, $E(\mathbb{Q})$ contains $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z} = \{O, (1,0), (0,0), (-1,0)\}$: the three points of order $2$ are the roots of the cubic.

**Example.** On $E: y^2 = x^3-x$ the point $(2,\sqrt6)$ lies on the curve, since $2^3-2 = 6$; but $\sqrt6 \notin \mathbb{Q}$, so it is a point of $E(\mathbb{Q}(\sqrt6))$ and not of $E(\mathbb{Q})$. Whether a given point is rational is a property of the base field, while the group law itself is defined over $\bar K$ throughout.

### Explicit Formulas

**Theorem.** In the short Weierstrass form $y^2 = x^3 + ax + b$, for $P_1 = (x_1,y_1)$ and $P_2 = (x_2,y_2)$ with $P_1, P_2 \neq O$ and $P_1 \neq \pm P_2$:

$$
\lambda = \frac{y_2-y_1}{x_2-x_1}, \qquad x_3 = \lambda^2 - x_1 - x_2, \qquad y_3 = -\lambda x_3 - (y_1 - \lambda x_1),
$$

and $P_1+P_2 = (x_3,y_3)$. For $P = (x,y) \neq O$ with $y \neq 0$:

$$
x(2P) = \frac{x^4 - 2ax^2 - 8bx + a^2}{4(x^3+ax+b)}, \qquad y(2P) = \lambda(x - x(2P)) - y, \qquad \lambda = \frac{3x^2+a}{2y}.
$$

The doubling formula is obtained from the addition formula at $x_1 = x_2 = x$, $y_1 = y_2 = y$ by the algebraic computation of the slope of the tangent line at $P$, namely $\lambda = (3x^2+a)/(2y)$; a direct expansion of $\lambda^2 - 2x$ with $y^2 = x^3+ax+b$ gives the displayed numerator.

**Example.** On $E: y^2 = x^3 - 2$ take $P = (3,5)$, which lies on the curve since $25 = 27-2$. Here $a = 0$, $b = -2$, so

$$
x(2P) = \frac{x^4 - 8bx + a^2}{4y^2} = \frac{81 + 48}{100} = \frac{129}{100}, \qquad \lambda = \frac{9}{10},
$$

and $y(2P) = \lambda(x - x(2P)) - y = \frac{27}{10}\left(3 - \frac{129}{100}\right) - 5 = \frac{27}{10}\cdot\frac{171}{100} - 5 = \frac{4617}{1000} - \frac{5000}{1000} = -\frac{383}{1000}$, so that $2P = \left(\frac{129}{100}, -\frac{383}{1000}\right)$. The result satisfies the curve equation: $y(2P)^2 = 383^2/10^6 = 146689/10^6$ and $x(2P)^3 - 2 = (129^3 - 2\cdot10^6)/10^6 = (2146689-2000000)/10^6 = 146689/10^6$.

**Theorem (structure of the torsion).** Let $E$ be an elliptic curve over $K$ and $n \geq 1$.

**(a)** If $\operatorname{char} K = 0$, or if $\operatorname{char} K = p > 0$ with $p \nmid n$, then $E[n] = \{P \in E(\bar K) : nP = O\} \cong (\mathbb{Z}/n\mathbb{Z})^2$ as abelian groups, and the action of $\operatorname{Gal}(\bar K/K)$ on $E[n]$ is a homomorphism $\operatorname{Gal}(\bar K/K) \to \operatorname{GL}_2(\mathbb{Z}/n\mathbb{Z})$.

**(b)** If $\operatorname{char} K = p > 0$ then $E[p] \cong \mathbb{Z}/p\mathbb{Z}$ — the **ordinary** case — or $E[p] = 0$ — the **supersingular** case.

**Proof sketch.** (a) For $n$ coprime to the characteristic the multiplication-by-$n$ map is separable of degree $n^2$ and the kernel is a free $\mathbb{Z}/n\mathbb{Z}$-module of rank $2$; the structure theorem for torsion abelian groups, together with the nondegeneracy of the differentiating argument at $O$, gives the isomorphism. (b) The kernel of Frobenius has order $p$ or $1$ in the supersingular case, and $E[p]$ is the kernel of the Verschiebung composed with Frobenius. $\square$

**Example.** For $E: y^2 = x^3 - x$ over $\mathbb{Q}$: $E[2] = \{O, (0,0), (1,0), (-1,0)\} \cong (\mathbb{Z}/2\mathbb{Z})^2$ and $E(\mathbb{Q}) = E[2]$, of rank $0$. For $E: y^2 = x^3 + 1$ over $\mathbb{F}_5$, which is supersingular, $E[5] = 0$.

---

## Endomorphisms and Isogenies

**Definition.** An **isogeny** $\phi : E_1 \to E_2$ is a morphism of curves carrying $O_1$ to $O_2$; it is automatically a group homomorphism. Its **degree** $\deg\phi$ is $[K(E_1):\phi^*K(E_2)]$ when nonzero, and $0$ for the zero map. An **endomorphism** of $E$ is a morphism $E \to E$ fixing $O$, and $\operatorname{End}(E)$ is the ring of endomorphisms with the group law as addition and composition as multiplication.

**Theorem.** Let $E$ be an elliptic curve over $K$.

**(a)** Every nonzero isogeny $\phi : E \to E'$ has a unique **dual isogeny** $\hat\phi : E' \to E$ with $\hat\phi\circ\phi = [\deg\phi]$; the degree is multiplicative, $(\widehat{\phi\psi}) = \hat\psi\hat\phi$, and $\deg\phi = \lvert\ker\phi\rvert$ when $\phi$ is separable.

**(b)** $\operatorname{End}(E)$ has no zero divisors, is free of finite rank over $\mathbb{Z}$, and $\operatorname{End}(E)\otimes\mathbb{Q}$ is of one of the following forms: $\mathbb{Q}$; an imaginary quadratic field; or, when $\operatorname{char} K = p > 0$, a four-dimensional central division algebra over $\mathbb{Q}$ (the quaternion case, treated in *Division Algebras*, in the algebra layer).

**(c)** The multiplication-by-$n$ endomorphism $[n]$ has degree $n^2$ and $\ker[n] = E[n]$, and the **Tate module** $T_\ell(E) = \varprojlim_n E[\ell^n]$, an inverse limit of finite groups taken algebraically, is a free $\mathbb{Z}_\ell$-module of rank $2$ on which $\operatorname{Gal}(\bar K/K)$ acts $\mathbb{Z}_\ell$-linearly, and $\operatorname{End}(E)\otimes\mathbb{Z}_\ell \hookrightarrow \operatorname{End}_{\mathbb{Z}_\ell}(T_\ell(E))$.

**Proof sketch.** (a) The dual isogeny is constructed by summing the pullbacks of the divisor classes, or by using the fact that the isogeny is a group homomorphism and the dual is the group-theoretic inverse up to degree; the identity $\hat\phi\phi = [\deg\phi]$ follows from the degree formula for a composition. (b) A nonzero endomorphism is surjective and hence has finite kernel; the rank is at most $4$ because an endomorphism of a one-dimensional group is determined up to a scalar by its action on $T_\ell$, which is a $2$-dimensional $\mathbb{Z}_\ell$-module. (c) The Tate module is the algebraic inverse limit of the $\ell^n$-torsion, and the rank statement is the structure theorem for $E[\ell^n]$. The Tate modules taken as topological objects, the $\ell$-adic representations as objects of functional analysis, and the completed endomorphism rings belong to Part II, where the completion is available. $\square$

**Theorem (complex multiplication).** Let $E$ over a field of characteristic $0$ have $\operatorname{End}(E) \neq \mathbb{Z}$. Then $\operatorname{End}(E)$ is an order in an imaginary quadratic field $F$, the curve is said to have **complex multiplication** by $F$, and its $j$-invariant is an algebraic integer; moreover the $j$-invariant of a curve with complex multiplication by an order $\mathcal{O}$ generates over $F$ a ring class field, abelian over $F$ by the reciprocity law of *Class Field Theory*, and this is the main theorem of complex multiplication. In a finite field of characteristic $p$ the endomorphism ring of a supersingular curve is a maximal order in a four-dimensional central division algebra over $\mathbb{Q}$, and of an ordinary curve an order in an imaginary quadratic field in which $p$ splits.

**Example.** The curve $y^2 = x^3 - x$ has $j = 1728 = 12^3$, and the automorphism $(x,y) \mapsto (-x, iy)$ over $\mathbb{Q}(i)$ is an endomorphism of degree $1$ with square $[-1]$; this is complex multiplication by $\mathbb{Z}[i]$. The curve $y^2 = x^3+1$ has $j = 0$ and admits the automorphism $(x,y) \mapsto (\zeta_3x,y)$ of order $3$; here $\operatorname{End}(E) \supseteq \mathbb{Z}[\zeta_3]$ and the curve has complex multiplication by $\mathbb{Q}(\zeta_3)$. Since $j=1728$ and $j = 0$ are rational integers, the two curves are defined over $\mathbb{Q}$, as the theory of complex multiplication predicts.

---

## Elliptic Curves over Finite Fields

### The Frobenius Endomorphism and the Hasse Bound

**Definition.** Let $E$ be an elliptic curve over $\mathbb{F}_q$. The **Frobenius endomorphism** is

$$
\pi : E \to E, \qquad (x,y) \mapsto (x^q, y^q),
$$

fixing $O$; it is a purely inseparable isogeny of degree $q$, and $E(\mathbb{F}_q) = \ker(\pi - 1)$.

**Theorem (Hasse).** Let $E$ be an elliptic curve over $\mathbb{F}_q$ and $a_q = q + 1 - \lvert E(\mathbb{F}_q)\rvert$. Then

$$
\lvert a_q \rvert \leq 2\sqrt q , \qquad \pi^2 - a_q\pi + q = 0 \quad \text{in } \operatorname{End}(E),
$$

so that $\pi$ satisfies $\pi\hat\pi = q$, with $\hat\pi$ the dual isogeny; the number $a_q$ is the trace $\pi + \hat\pi$ and $q$ is the norm $\pi\hat\pi$, and the displayed inequality is equivalent to the positivity of the degrees $\deg(\pi-m) = m^2-a_qm+q$ for all integers $m$, which is the elementary proof of the bound.

**Proof sketch.** The relation $\pi^2 - a_q\pi + q = 0$ is proved by comparing degrees in $\operatorname{End}(E)$, using $\deg(\pi - 1) = \lvert E(\mathbb{F}_q)\rvert$ together with the identity $\deg(\pi-m) = \deg\pi - m(\pi + \hat\pi) + m^2$ for the reduced trace; the bound then follows from the positivity of the degrees $\deg(\pi - m) \geq 0$ at suitable integers $m$, since $\pi\bar\pi = q$ forces $a_q^2 \leq 4q$; no analysis enters. The same bound is the genus-one case of the Riemann hypothesis for the zeta function of a curve, whose analytic formulation is stated, and belongs to Part III. $\square$

**Definition.** For an elliptic curve $E$ over $\mathbb{F}_q$ the **zeta function** is

$$
Z(E/\mathbb{F}_q, T) = \exp\left(\sum_{n\geq1}\lvert E(\mathbb{F}_{q^n})\rvert\frac{T^n}{n}\right) = \frac{1 - a_qT + qT^2}{(1-T)(1-qT)} ,
$$

and the equality of the last two expressions, together with the bound $\lvert a_q\rvert \leq 2\sqrt q$, is the Riemann hypothesis for $E$. Here $\exp$ is the formal exponential series and the identity is an identity of formal power series, so no convergence or limit is involved.

**Example.** For $E: y^2 = x^3 - x$ over $\mathbb{F}_5$ the affine points are, by direct enumeration, $(0,0)$, $(1,0)$, $(2,1)$, $(2,4)$, $(3,2)$, $(3,3)$, $(4,0)$, seven of them, so $\lvert E(\mathbb{F}_5)\rvert = 8$, $a_5 = 5+1-8 = -2$, and $\lvert a_5\rvert = 2 < 2\sqrt5 \approx 4.47$. For $E: y^2 = x^3+1$ over $\mathbb{F}_5$: the affine points are $(0,1)$, $(0,4)$, $(2,3)$, $(2,2)$, $(4,0)$, five of them, so $\lvert E(\mathbb{F}_5)\rvert = 6$ and $a_5 = 0$, which is the supersingular case.

**Example.** For $E: y^2 = x^3+1$ over $\mathbb{F}_7$: the count of affine points is $2$ at $x = 0$, $2$ at $x = 1$ (since $2$ is a square modulo $7$, with roots $\pm3$), $2$ at $x = 2$ (since $9 \equiv 2$), $1$ at $x = 3$ (where the value is $0$), $2$ at $x = 4$ (where $65 \equiv 2$), $1$ at $x = 5$ (where $126 \equiv 0$) and $1$ at $x = 6$ (where $217 \equiv 0$), giving $11$ affine points and $\lvert E(\mathbb{F}_7)\rvert = 12$, so $a_7 = -4$ and $\lvert a_7\rvert = 4 < 2\sqrt7 \approx 5.29$; the number of points is reduced modulo $7$: $a_7 \equiv 7+1-12 = -4 \equiv 3 \not\equiv 0$, so the curve is ordinary over $\mathbb{F}_7$.

### Ordinary and Supersingular Curves

**Definition.** An elliptic curve over a field of characteristic $p > 0$ is **supersingular** if $E[p] = 0$, equivalently if $\operatorname{End}(E)\otimes\mathbb{Q}$ is a four-dimensional central division algebra over $\mathbb{Q}$, equivalently if $E$ has no point of order $p$ over $\bar K$; it is **ordinary** otherwise, that is, if $E[p] \cong \mathbb{Z}/p\mathbb{Z}$.

**Theorem.** Let $E$ over $\mathbb{F}_q$ with $q = p^f$.

**(a)** $E$ is supersingular if and only if $p \mid a_q$; for $p \geq 5$ this happens for only finitely many $j$-invariants, all lying in $\mathbb{F}_{p^2}$.

**(b)** If $E$ runs over the elliptic curves over $\mathbb{F}_q$, the values $a_q$ are distributed in the interval $[-2\sqrt q, 2\sqrt q]$ and the number of isomorphism classes with a given trace is finite; the explicit equidistribution is an analytic statement, the **Sato–Tate** statement, and is not available in this Part.

**(c)** Every elliptic curve over $\mathbb{F}_q$ is isogenous to one defined over $\mathbb{F}_p$ when it is supersingular; more generally the isogeny classes over $\mathbb{F}_q$ are classified by the characteristic polynomial $T^2-a_qT+q$ of Frobenius, by Tate's isogeny theorem, whose proof uses the Tate module as a module over a completion and hence belongs to Part II.

**Example.** The curve $y^2 = x^3+1$ over $\mathbb{F}_5$ has $a_5 = 0$, hence is supersingular, consistent with $5 \equiv 2 \bmod 3$ and $j = 0$; the curve $y^2 = x^3-x$ over $\mathbb{F}_5$ has $a_5 = -2$, not divisible by $5$, hence ordinary.

---

## Arithmetic over Number Fields

### Mordell–Weil and Nagell–Lutz

**Theorem (Mordell–Weil).** Let $K$ be a number field and $E$ an elliptic curve over $K$. Then $E(K)$ is a finitely generated abelian group,

$$
E(K) \cong \mathbb{Z}^r \oplus E(K)_{\mathrm{tors}},
$$

where $r$ is the **rank** of $E$ over $K$ and $E(K)_{\mathrm{tors}}$ the finite torsion subgroup. The proof proceeds in two steps: the **weak Mordell–Weil theorem**, that $E(K)/mE(K)$ is finite for every $m \geq 2$, proved by Kummer theory of *Kummer Theory* applied to the extension $K(E[m])/K$; and the descent argument, which uses the theory of heights. **A height is built from absolute values**, so its theory, and with it the second step of the proof, belongs to Part II, where absolute values and their products over the places are available; the statement is recorded here.

**Theorem (Nagell–Lutz).** Let $E$ be given by $y^2 = x^3 + ax + b$ with $a, b \in \mathbb{Z}$, and let $P = (x,y) \in E(\mathbb{Q})$ with $P \neq O$.

**(a)** If $P$ is a torsion point, then $x, y \in \mathbb{Z}$.

**(b)** If $P$ has order $n > 2$, then $y^2$ divides $4a^3+27b^2$.

**Proof sketch.** (a) Reducing the equation modulo a prime $\ell$ and using that $P$ reduces to a point of the finite group $E(\mathbb{F}_\ell)$ shows that the denominators of $x$ and $y$ are bounded; a more precise argument with the $\ell$-adic valuation of the coordinates at a prime dividing the denominator contradicts the finiteness of the order of $P$ in $E(\mathbb{Q}_\ell)$, or in the algebraic language, in the image of $E(\mathbb{Q})$ in $E(\mathbb{F}_\ell)$. (b) is the integrality together with the discriminant criterion for the doubling formula. $\square$

**Example.** On $E: y^2 = x^3 - 2$, the point $(3,5)$ is not torsion, by (a) and (b): $y = 5$ and $y^2 = 25$ does not divide $4a^3+27b^2 = 4\cdot0 + 27\cdot4 = 108$, so $(3,5)$ has infinite order. On $E: y^2 = x^3 - x$, the point $(0,0)$ is torsion of order $2$, with $y = 0$, consistent with (b).

### Torsion and Reduction

**Theorem (Mazur).** Let $E$ be an elliptic curve over $\mathbb{Q}$. Then $E(\mathbb{Q})_{\mathrm{tors}}$ is isomorphic to one of the fifteen groups

$$
\mathbb{Z}/n\mathbb{Z}\ (1 \leq n \leq 10,\ n = 12), \qquad (\mathbb{Z}/2\mathbb{Z})\times(\mathbb{Z}/2n\mathbb{Z})\ (1 \leq n \leq 4).
$$

**Theorem (reduction).** Let $K$ be a number field, $\mathfrak{p}$ a nonzero prime of $\mathcal{O}_K$ of residue characteristic $p$, and $E$ an elliptic curve over $K$ with a Weierstrass equation integral at $\mathfrak{p}$ whose discriminant is not divisible by $\mathfrak{p}$, so that the reduced equation is nonsingular and defines an elliptic curve $\tilde E$ over $\kappa(\mathfrak{p})$. Then the reduction map $E(K) \to \tilde E(\kappa(\mathfrak{p}))$ is injective on the torsion subgroup of order coprime to $p$, and

$$
\lvert E(K)_{\mathrm{tors}}\rvert \ \text{divides}\ \ \lvert \tilde E(\kappa(\mathfrak{p}))\rvert \ \text{whenever}\ \mathfrak{p}\nmid \lvert E(K)_{\mathrm{tors}}\rvert .
$$

**Example.** For $E: y^2 = x^3 - x$ over $\mathbb{Q}$ and $\mathfrak{p} = (5)$, the reduced curve over $\mathbb{F}_5$ has $8$ points, and indeed $E(\mathbb{Q})_{\mathrm{tors}} = (\mathbb{Z}/2\mathbb{Z})^2$ of order $4$ divides $8$. For $E: y^2 = x^3 - x$ and $\mathfrak{p} = (3)$, the reduced curve over $\mathbb{F}_3$ has $\lvert E(\mathbb{F}_3)\rvert = 4$ points (the affine points being $(0,0)$, $(1,0)$, $(2,0)$, plus $O$), and the reduction of the torsion of order $4$ is injective.

**Remark.** The finer theory of the reduction type — good, multiplicative, additive reduction, the Kodaira–Néron classification, the conductor of $E$ and the criterion of Néron–Ogg–Shafarevich — is local at a place and requires the completion of $K$ at $\mathfrak{p}$, and is therefore treated in Part II together with the local field that carries it.

---

## Summary

An elliptic curve over a field $K$ is a nonsingular projective curve of genus $1$ with a rational point, equivalently a nonsingular Weierstrass equation $y^2+a_1xy+a_3y = x^3+a_2x^2+a_4x+a_6$; its discriminant $\Delta$ is nonzero, its $j$-invariant $c_4^3/\Delta$ classifies it up to isomorphism over an algebraically closed field, and over a general field the isomorphism classes with a given $j$-invariant are classified by the cohomology of the finite automorphism group. The points form an abelian group under the chord–tangent law, given by rational functions with coefficients in $K$; the formulas are explicit, and the doubling formula in the short form $y^2 = x^3+ax+b$ is $x(2P) = (x^4-2ax^2-8bx+a^2)/(4y^2)$.

The torsion is $E[n] \cong (\mathbb{Z}/n\mathbb{Z})^2$ when $n$ is coprime to the characteristic, and $E[p]$ is $0$ or $\mathbb{Z}/p\mathbb{Z}$ according as the curve is supersingular or ordinary. Endomorphisms form a ring without zero divisors of finite rank over $\mathbb{Z}$, the dual isogeny satisfies $\hat\phi\phi = [\deg\phi]$, and $\operatorname{End}(E)\otimes\mathbb{Q}$ is $\mathbb{Q}$, an imaginary quadratic field, or a four-dimensional central division algebra over $\mathbb{Q}$; curves of the second kind have complex multiplication. Over $\mathbb{F}_q$ the Frobenius endomorphism $\pi$ has $\pi^2-a_q\pi+q = 0$ with $a_q = q+1-\lvert E(\mathbb{F}_q)\rvert$ and $\lvert a_q\rvert \leq 2\sqrt q$, and the zeta function of $E$ is the rational function $(1-a_qT+qT^2)/((1-T)(1-qT))$ with the equality of formal power series giving the point counts over all $\mathbb{F}_{q^n}$.

Over a number field $E(K)$ is finitely generated by Mordell–Weil, with the descent step deferred to the Part that has heights; the torsion is pinned by Nagell–Lutz, by Mazur's classification of the fifteen possible torsion groups over $\mathbb{Q}$, and by the reduction map at a prime of good reduction. The local theory of reduction, the completed Tate module, the $L$-function and the analytic distribution of the traces $a_q$ belong to later Parts.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Base field |
| $\bar K$ | An algebraic closure of $K$ |
| $E$, $E'$ | Elliptic curves |
| $O$ | The point at infinity, the identity of $E(K)$ |
| $a_1,a_2,a_3,a_4,a_6$ | Weierstrass coefficients |
| $b_2,b_4,b_6,b_8$ | The usual auxiliary quantities |
| $\Delta$, $c_4$ | Discriminant, a second invariant |
| $j$ | $j$-invariant $c_4^3/\Delta$ |
| $E(K)$, $E(\bar K)$ | Groups of rational, algebraic points |
| $E[n]$ | The $n$-torsion subgroup |
| $[n]$ | Multiplication-by-$n$ endomorphism |
| $\operatorname{End}(E)$ | Endomorphism ring |
| $\phi, \hat\phi, \deg\phi$ | Isogeny, dual isogeny, degree |
| $T_\ell(E)$ | Tate module $\varprojlim_n E[\ell^n]$ |
| $\pi$ | Frobenius endomorphism over $\mathbb{F}_q$ |
| $a_q$ | $q+1-\lvert E(\mathbb{F}_q)\rvert$, the trace of $\pi$ |
| $Z(E/\mathbb{F}_q,T)$ | Zeta function of $E$ |
| $E(K)_{\mathrm{tors}}$ | Torsion subgroup |
| $r$ | Rank of $E(K)$ |
| $\tilde E$, $\kappa(\mathfrak{p})$ | Reduced curve, residue field |
| $\lambda$ | Slope of a chord or tangent; also the Legendre parameter |



## Further Reading

- Joseph H. Silverman, *The Arithmetic of Elliptic Curves* (Springer, 2nd ed. 2009), for the group law, the torsion, the isogenies, the Tate module and the arithmetic of elliptic curves.
- Joseph H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (Springer, 1994), for complex multiplication, the local theory and the $L$-function.
- Anthony W. Knapp, *Elliptic Curves* (Princeton University Press, 1992), for a treatment of the group law and the Mordell–Weil theorem with the analytic and geometric background.
- Helmut Hasse, "Zur Theorie der abstrakten elliptischen Funktionenkörper I–III", *Journal für die reine und angewandte Mathematik* 175 (1936), 55–62, 69–88, 193–208, for the Frobenius, the point count and the bound $\lvert a_q\rvert \leq 2\sqrt q$.
- André Weil, "Sur les courbes algébriques et les variétés qui s'en déduisent" (Hermann, 1948), for the proof of the Riemann hypothesis for curves and the bound on the point count.
- Barry Mazur, "Modular curves and the Eisenstein ideal", *Publications mathématiques de l'IHÉS* 47 (1977), 33–186, for the classification of the torsion of elliptic curves over $\mathbb{Q}$.
- John Tate, "Endomorphisms of abelian varieties over finite fields", *Inventiones Mathematicae* 2 (1966), 134–144, for the isogeny theorem and the classification of the characteristic polynomials of Frobenius.
- Trygve Nagell, "Solutions de quelques équations dans des corps de caractéristique finie", *Norsk Matematisk Forenings Skrifter* 13 (1921), and Élisabeth Lutz, "Sur l'équation $y^2 = x^3 - Ax - B$ dans les corps $p$-adiques", *Journal für die reine und angewandte Mathematik* 175 (1936), 237–247, for the integrality of torsion points.
