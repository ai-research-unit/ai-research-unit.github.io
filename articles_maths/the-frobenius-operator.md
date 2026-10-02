
# __The Frobenius Operator__

## Introduction

In characteristic $p$ the map that raises a function to its $p$-th power is additive, and on a variety over a finite field it is a morphism of the variety to itself that is the identity on the underlying points and yet changes the functions. This article reads that map, the **Frobenius**, as the third operator of the category. It fixes the absolute Frobenius, its relative form and the Frobenius twist, proves the $p$-linearity that makes the map an operator rather than a multiplication, computes its fixed points, and records the way the fixed points of its powers are the arithmetic of the variety: the zeta function is assembled from them, and the statements of the Weil conjectures are the statements about the Frobenius operators on the cohomology.

The article is the third of the `- Operator Theory` group. Its neighbour *The Galois Action as an Operator* is the same kind of operator over a general field, and the Frobenius is the Galois operator in the case of a finite base field, where the group has a canonical generator; the field-level map is Part I's *The Frobenius Operator on a Field of Characteristic p* and *The Frobenius Automorphism of a Finite Field*, written elsewhere in the corpus. The arithmetic of the fixed points on a curve, the L-functions and the modularity belong to the number theory of Parts I and III.

Throughout $p$ is a prime, $q = p^a$, $k = \mathbb{F}_q$, and $X$ is a variety over $k$ — the hypothesis of finite type over a finite field is kept throughout, since the interesting theorems are arithmetic and false for a general base. The structure sheaf is $\mathcal{O}_X$ and $\mathcal{O}_X(U)$ is a ring of characteristic $p$.

## The Frobenius Endomorphism

**Definition.** The **absolute Frobenius** of $X$ is the morphism
$$
F = F_X : X\longrightarrow X
$$
which is the identity on the underlying topological space and whose pullback on functions is the $p$-th power map,
$$
F^* : \mathcal{O}_X(U)\longrightarrow\mathcal{O}_X(U), \qquad F^*(f) = f^p .
$$

**Proposition ($F$ is a morphism, and it is not the identity).** The map $F^*$ is an endomorphism of each ring $\mathcal{O}_X(U)$, so $F$ is a morphism of schemes; it is additive because
$$
(f+g)^p = f^p + \binom{p}{1}f^{p-1}g + \cdots + g^p = f^p + g^p ,
$$
all the intermediate binomial coefficients being divisible by $p$. The morphism $F$ is an isomorphism precisely when $X$ is reduced and the absolute Frobenius of each residue field is onto, which for a variety over $\mathbb{F}_q$ means that $X$ is a disjoint union of points; on any variety of positive dimension $F$ is a finite surjective morphism of degree $p^{\dim X}$ and not an isomorphism.

*Proof.* Additivity is the displayed binomial computation, multiplicativity is automatic for a power map, so $F^*$ is a ring endomorphism, and a morphism of locally ringed spaces is a ring map in the opposite direction; the topological part is the identity. A morphism that is the identity on points and not the identity on functions can still be an isomorphism of schemes only if the map on every local ring is bijective; the failure on a curve is exhibited in the example below.

**Remark (the Frobenius is not an operator of the layer of *Operators on a Variety*).** The multiplication operators of the structure sheaf are $\mathcal{O}_X$-linear, while $F^*$ is a ring endomorphism that is not $\mathcal{O}_X$-linear: for a function $f$ and a constant $\lambda$,
$$
F^*(\lambda f) = \lambda^p f^p = \lambda^p\,F^*(f) .
$$
On the constants $F^*$ is the Frobenius of the field. The map is therefore **$p$-linear** rather than linear, and it is an endomorphism of the operator layer as a ring, not an element of the layer. This is the same phenomenon as the semilinearity of the Galois action, in its sharpest characteristic-$p$ form.

**Example ($\mathbb{A}^1$ and $\mathbb{P}^1$).** On $X = \mathbb{A}^1_{\mathbb{F}_q}$ the absolute Frobenius is the morphism with $F^*(t) = t^p$, so it is the endomorphism $t\mapsto t^p$ of the affine line. On $\mathbb{P}^1$ the same formula $[x_0:x_1]\mapsto[x_0^p:x_1^p]$ is well defined on homogeneous coordinates. Both are bijective on points over an algebraically closed field and are not isomorphisms.

## The Relative Frobenius and the Frobenius Twist

**Definition.** Write $X^{(p)} = X\times_{\operatorname{Spec}\mathbb{F}_p,\ F_{\mathbb{F}_p}}\operatorname{Spec}\mathbb{F}_p$ for the **Frobenius twist** of $X$, the base change of $X$ along the Frobenius of the prime field. The **relative Frobenius** is the morphism
$$
F_{X/\mathbb{F}_p} : X\longrightarrow X^{(p)}
$$
over $\mathbb{F}_p$ whose two components are $F_X$ and the structure map $X\to\operatorname{Spec}\mathbb{F}_p$; it is a morphism of $\mathbb{F}_p$-schemes, and over a perfect field with $q = p$ it is an isomorphism exactly when $X$ is reduced.

**Definition.** The **$q$-power Frobenius** is the $a$-th power of the absolute Frobenius,
$$
\pi = F^a : X\longrightarrow X, \qquad \pi^*(f) = f^{q} .
$$

**Proposition ($\pi$ is a morphism over $\mathbb{F}_q$).** The $q$-power Frobenius is $\mathbb{F}_q$-linear: for $\lambda\in\mathbb{F}_q$ one has $\lambda^q = \lambda$, so
$$
\pi^*(\lambda f) = \lambda^q f^q = \lambda\,\pi^*(f) .
$$
Hence $\pi$ is a morphism of $X$ over $k = \mathbb{F}_q$, and it is the operator of the $k$-structure of $X$, while the absolute Frobenius $F$ is only a morphism over $\mathbb{F}_p$.

*Proof.* The identity $\lambda^q = \lambda$ for $\lambda\in\mathbb{F}_q$ is the statement that $\mathbb{F}_q$ is the fixed field of the Frobenius (Part I's *Finite Fields* and *The Frobenius Automorphism of a Finite Field*); the displayed computation then shows that $\pi^*$ commutes with the $k$-scalars, which is what it means for $\pi$ to be a $k$-morphism.

**Example ($\mathbb{F}_{q^n}$ and Frobenius powers).** For the field $k = \mathbb{F}_q$ itself, $X = \operatorname{Spec}\mathbb{F}_q$, the $q$-power Frobenius satisfies $\pi^* = \mathrm{id}$ on $\mathbb{F}_q$, so $\pi = \mathrm{id}$, while the absolute Frobenius is the field automorphism $x\mapsto x^p$, of order $a$. On $X = \operatorname{Spec}\mathbb{F}_{q^n}$ the $q$-power Frobenius generates the cyclic group $\operatorname{Gal}(\mathbb{F}_{q^n}/\mathbb{F}_q)$ of order $n$; this is the operator-level form of the statement of *Finite Fields* that a finite field is its own splitting field for the polynomials $x^{q^n}-x$.

## Fixed Points

**Definition.** For a variety $X$ over $k$, the **fixed subscheme** of an endomorphism $\varphi : X\to X$ is the equaliser of $\varphi$ and the identity, that is, the fibre product of the diagonal $X\to X\times_kX$ with the graph $(\mathrm{id},\varphi) : X\to X\times_kX$; it is the locus cut out by the vanishing of the difference of the two maps. On the points with values in a $k$-algebra $R$, the fixed points of $\varphi$ are the elements of $X(R)$ fixed by the induced map.

**Theorem (fixed points of the Frobenius powers).** Let $X$ be a variety over $\mathbb{F}_q$ and let $\pi = F^a$ be its $q$-power Frobenius. For every $n\geq1$,
$$
X(\bar{\mathbb{F}}_q)^{\pi^n} = X(\mathbb{F}_{q^n}) ,
$$
the set of points with values in the field with $q^n$ elements. In particular the fixed points of $\pi$ are the $\mathbb{F}_q$-points, $X(\bar{\mathbb{F}}_q)^{\pi} = X(\mathbb{F}_q)$.

*Proof.* The $q^n$-power Frobenius on $\bar{\mathbb{F}}_q$ has fixed field $\mathbb{F}_{q^n}$, since the roots of $x^{q^n}-x$ are exactly that field (Part I's *Finite Fields*). A point $P : \operatorname{Spec}\bar{\mathbb{F}}_q\to X$ is fixed by $\pi^n$ precisely when the corresponding $\bar{\mathbb{F}}_q$-algebra homomorphism lands in the fixed field of $\pi^n$, by the same argument as in *The Galois Action as an Operator* for the fixed points of a Galois action; that fixed field is $\mathbb{F}_{q^n}$, so the fixed points are the $\mathbb{F}_{q^n}$-points.

**Corollary (finiteness).** Each set $X(\mathbb{F}_{q^n})$ is finite, and it is empty for $n$ negative in the sense that $X(\mathbb{F}_{q^n})$ is the set of closed points of $X$ whose degree divides $n$.

*Proof.* A variety of finite type over a finite field has finitely many closed points of each degree, and an $\mathbb{F}_{q^n}$-point has residue field a finite extension of $\mathbb{F}_{q^n}$, hence one of the finitely many fields $\mathbb{F}_{q^{nm}}$; the count of points of each degree is finite because $X$ is of finite type over a finite field.

## The Frobenius on Cohomology

**Proposition (the action on cohomology).** The Frobenius $\pi$ is an endomorphism of $X$ over $k$, so by *Operators on a Variety* it acts on the cohomology of a quasi-coherent sheaf by
$$
\pi^* : H^i(X,\mathcal{F})\longrightarrow H^i(X,\pi^*\mathcal{F}) ,
$$
and on $H^i(X,\mathcal{O}_X)$ by an endomorphism that is $k$-linear. More generally the assignment $n\mapsto\pi^{n*} = (F^n)^{a*}$ is a representation of the monoid $\mathbb{N}$ by $k$-linear endomorphisms of $H^i(X,\mathcal{O}_X)$, and the Lefschetz number of each power,
$$
L(\pi^n) = \sum_i(-1)^i\operatorname{tr}\bigl(\pi^{n*}\mid H^i(X,\mathcal{O}_X)\bigr) ,
$$
is defined.

*Proof.* Functoriality of cohomology gives the map and the multiplicativity $(\pi^n)^* = (\pi^*)^n$, and $k$-linearity is the previous section. The trace is the trace of a $k$-linear endomorphism of a finite-dimensional space whenever the cohomology is finite-dimensional, which is the case for the structure sheaf of a projective variety over a field by *Coherent Sheaves*.

**Remark (the cohomology that carries the fixed points).** The Zariski cohomology of the structure sheaf is not the cohomology in which the fixed-point theorem for the Frobenius holds: a theorem of this kind needs a cohomology with the base change and the cycle-class properties, the **étale cohomology** with $\ell$-adic coefficients for a prime $\ell\neq p$. That theory is not developed in this Part, and the statements below are recorded as the conjectures of Weil, which are the properties its Frobenius action must have; the reader will find the construction in the literature cited under *Further Reading*.

**Theorem (the Lefschetz fixed-point formula, conjectural form).** For a separated variety $X$ of finite type over $\mathbb{F}_q$ there is a finite-dimensional $\ell$-adic cohomology with a $k$-linear action of $\pi$ such that
$$
|X(\mathbb{F}_{q^n})| = \sum_i(-1)^i\operatorname{tr}\bigl(\pi^{n*}\mid H^i_{\mathrm{ét}}(X_{\bar{\mathbb{F}}_q},\mathbb{Q}_\ell)\bigr)
$$
for every $n\geq1$. This is the fixed-point theorem whose left side is the fixed set of the previous section and whose right side is an alternating trace of the operator on cohomology, in the form in which the corpus records it.

## The Zeta Function and the Weil Conjectures

**Definition.** The **zeta function** of a variety $X$ of finite type over $\mathbb{F}_q$ is the formal power series
$$
Z(X,t) = \prod_{x\in X_{\mathrm{cl}}}\bigl(1-t^{\deg(x)}\bigr)^{-1}\ \in\ \mathbb{Z}[[t]] ,
$$
the product running over the closed points of $X$, with $\deg(x) = [\kappa(x):\mathbb{F}_q]$ the degree of the residue field of $x$. The coefficients are integers because there are finitely many closed points of each degree.

**Theorem (the bridge to the point counts).** The zeta function is the formal exponential of the point counts,
$$
Z(X,t) = \exp\Bigl(\sum_{n\geq1}|X(\mathbb{F}_{q^n})|\,\frac{t^n}{n}\Bigr),
$$
so that the arithmetic of the fixed points of the Frobenius powers determines the zeta function and conversely.

*Proof.* Expanding each factor $\bigl(1-t^{\deg x}\bigr)^{-1} = \sum_{m\geq0}t^{m\deg x}$ and taking the formal logarithm gives
$$
-\sum_{x\in X_{\mathrm{cl}}}\log\bigl(1-t^{\deg x}\bigr) = \sum_{x\in X_{\mathrm{cl}}}\sum_{m\geq1}\frac{t^{m\deg x}}{m} = \sum_{n\geq1}\Bigl(\sum_{\deg(x)\mid n}\deg(x)\Bigr)\frac{t^n}{n} = \sum_{n\geq1}|X(\mathbb{F}_{q^n})|\frac{t^n}{n},
$$
because the points of $X(\mathbb{F}_{q^n})$ are exactly the closed points whose degree divides $n$, counted with the degree of their residue field extension. Exponentiating the identity gives the displayed form, with $\log(1-u) = -\sum_{m\geq1}u^m/m$ and $\exp$ the formal inverse pair over $\mathbb{Q}$.

**Theorem (the Weil conjectures).** Let $X$ be a smooth projective variety of dimension $d$ over $\mathbb{F}_q$. Then the following properties hold for the zeta function and the Frobenius operators on the $\ell$-adic cohomology.

1. **Rationality.** $Z(X,t)$ is a rational function of $t$ and
   $$
   Z(X,t) = \frac{P_1(t)\cdots P_{2d-1}(t)}{P_0(t)\,P_2(t)\cdots P_{2d}(t)}, \qquad P_i(t) = \det\bigl(1 - t\,\pi^*\mid H^i_{\mathrm{ét}}(X_{\bar{\mathbb{F}}_q},\mathbb{Q}_\ell)\bigr) ,
   $$
   with $P_i\in\mathbb{Z}[t]$ and $P_0(t) = 1-t$, $P_{2d}(t) = 1-q^dt$, and $\deg P_i$ the $i$-th Betti number of $X$.
2. **Functional equation.** Writing $\chi = \sum_i(-1)^i\deg P_i$ for the Euler characteristic,
   $$
   Z\bigl(X,1/(q^dt)\bigr) = \pm\,q^{d\chi/2}\,t^{\chi}\,Z(X,t).
   $$
3. **Riemann hypothesis.** Each root $\alpha$ of $P_i$ is an algebraic integer with every archimedean absolute value equal to $q^{i/2}$: the eigenvalues of $\pi^*$ on $H^i_{\mathrm{ét}}$ have absolute value $q^{i/2}$.

*Proof.* The three statements are the conjectures of Weil, proved by the comparison of the three operators of the Lefschetz formula with the cycle class and the Poincaré duality of the étale theory; the rationality follows from the Lefschetz formula and the finite-dimensionality of the cohomology, the functional equation from Poincaré duality together with the degree of the Frobenius action on the top cohomology, and the third from the positivity of the intersection form, which is the sharpest step. The proofs are not reproduced here, the cohomology theory not being available in this Part; the statements are recorded because the Frobenius is their operator.

**Example (the projective line).** For $X = \mathbb{P}^1_{\mathbb{F}_q}$ one has $|X(\mathbb{F}_{q^n})| = q^n+1$, so
$$
Z(\mathbb{P}^1,t) = \frac{1}{(1-t)(1-qt)} , \qquad P_0(t) = 1-t, \quad P_2(t) = 1-qt ,
$$
with $P_1 = 1$, $\chi = 2$, and the functional equation $Z(1/(qt)) = q\,t^2\,Z(t)$ exact rather than up to sign. The absolute values are $1$ on $H^0$ and $q$ on $H^2$, in accordance with $|\alpha| = q^{i/2}$ at $i = 0,2$.

**Example (an elliptic curve).** For an elliptic curve $E$ over $\mathbb{F}_q$ the point counts satisfy $|E(\mathbb{F}_{q^n})| = q^n+1 - \alpha^n - \bar{\alpha}^n$ for the two roots of $P_1$, and
$$
Z(E,t) = \frac{1-\alpha t}{1-t}\cdot\frac{1-\bar{\alpha}t}{1-qt} , \qquad \alpha\bar\alpha = q ,
$$
so the Riemann hypothesis $|\alpha| = \sqrt{q}$ is the arithmetic bound on the number of points of an elliptic curve over a finite field. The elliptic curves themselves, their group law and the L-function are Part I's *Elliptic Curves* and Part III's number theory, and are referenced rather than developed.

## Summary

In characteristic $p$ the $p$-th power map is additive, and it defines the **absolute Frobenius** $F_X : X\to X$, the identity on the underlying points and $f\mapsto f^p$ on functions; its $a$-th power is the **$q$-power Frobenius** $\pi$, a morphism over $\mathbb{F}_q$ that is $\mathbb{F}_q$-linear, and its relative form $F_{X/\mathbb{F}_p} : X\to X^{(p)}$ is the comparison with the Frobenius twist. The Frobenius is an endomorphism of the structure sheaf that is $p$-linear and not $\mathcal{O}_X$-linear, hence an endomorphism of the operator layer rather than an element of it, exactly as the Galois action is semilinear. Its fixed points are the arithmetic of the variety: the fixed points of $\pi^n$ on the geometric points are the $\mathbb{F}_{q^n}$-points, $X(\bar{\mathbb{F}}_q)^{\pi^n} = X(\mathbb{F}_{q^n})$, and these counts determine the zeta function $Z(X,t) = \prod_{x}(1-t^{\deg x})^{-1}$ and are determined by it. The Weil conjectures say that $Z$ is a rational function whose numerator and denominator factors are the characteristic polynomials of $\pi^*$ on the étale cohomology of $X$, that it satisfies a functional equation, and that the eigenvalues of $\pi^*$ on $H^i$ have absolute value $q^{i/2}$; the Frobenius is the operator on which all three statements turn, and the cohomological proofs lie outside this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p$, $q=p^a$, $k=\mathbb{F}_q$ | prime, its power, the finite base field |
| $F=F_X$ | absolute Frobenius: identity on points, $f\mapsto f^p$ on functions |
| $(f+g)^p=f^p+g^p$ | additivity of the Frobenius in characteristic $p$ |
| $X^{(p)}$, $F_{X/\mathbb{F}_p}:X\to X^{(p)}$ | Frobenius twist and relative Frobenius |
| $\pi=F^a$, $\pi^*(f)=f^q$ | $q$-power Frobenius, a morphism over $\mathbb{F}_q$ |
| $F^*(\lambda f)=\lambda^pF^*(f)$ | $p$-linearity: not an operator of the layer |
| $X(\bar{\mathbb{F}}_q)^{\pi^n}=X(\mathbb{F}_{q^n})$ | fixed points of the Frobenius powers |
| $L(\pi^n)=\sum_i(-1)^i\operatorname{tr}(\pi^{n*}\vert H^i)$ | Lefschetz number |
| $H^i_{\mathrm{ét}}(X_{\bar{\mathbb{F}}_q},\mathbb{Q}_\ell)$ | étale cohomology, the cohomology of the fixed-point formula (outside this Part) |
| $Z(X,t)=\prod_{x\in X_{\mathrm{cl}}}(1-t^{\deg x})^{-1}$ | zeta function of a variety over $\mathbb{F}_q$ |
| $\deg(x)=[\kappa(x):\mathbb{F}_q]$ | degree of a closed point |
| $P_i(t)=\det(1-t\pi^*\vert H^i_{\mathrm{ét}})$ | the numerator and denominator factors of $Z$ |
| $\vert\alpha\vert=q^{i/2}$ | the Riemann hypothesis for the Frobenius eigenvalues |

## Further Reading

- André Weil, *Numbers of solutions of equations in finite fields* (Bulletin of the American Mathematical Society 55, 1949), for the original conjectures and the zeta function of a variety.
- Pierre Deligne, *La conjecture de Weil I* (Publications Mathématiques de l'IHÉS 43, 1974), for the proof of the Riemann hypothesis for the Frobenius eigenvalues.
- Bernard Dwork, *On the rationality of the zeta function of an algebraic variety* (American Journal of Mathematics 82, 1960), for the rationality of the zeta function.
- Alexander Grothendieck, *Formule de Lefschetz et rationalité des fonctions L* (Séminaire Bourbaki, 1964), for the Lefschetz formula in étale cohomology.
- James S. Milne, *Lectures on Étale Cohomology* (v4.02, 2013), for the construction and properties of the cohomology in which the Frobenius acts.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the Frobenius morphism, the Frobenius twist and the elementary properties of a variety over a finite field.
- Michael Artin and Barry Mazur, *Etale Homotopy* (Springer Lecture Notes in Mathematics 100, 1969), for the homotopical reading of the Frobenius action.
