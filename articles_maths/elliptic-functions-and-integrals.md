
# __Elliptic Functions and Integrals__

## Introduction

This article stands in *Analysis on Rings and Fields*, immediately after *Analytic Functions and Power Series*, and it is the analysis of the elliptic functions: the functions obtained by inverting the elliptic integrals, together with the integrals themselves. The base is the complex field $\mathbb{C}$ with its usual absolute value, a complete valued field of characteristic zero, so that every result of *Analytic Functions and Power Series*, above, applies; the elliptic curves are Part I objects and belong to *Elliptic Curves*, where the group law is established algebraically, and this article supplies the analytic content of that group law without repeating it. The modular forms themselves are *Modular Forms*, below this article in this Part, and are not developed here: what this article supplies to that one is the period lattice, the modular parameter and the elliptic integrals.

The symbol $\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$ denotes a period lattice throughout, as the shared block fixes, and the notation is local to this article. The letter $G$, which is a group everywhere else in the corpus, denotes Catalan's constant in exactly one paragraph below, where it is defined, and nowhere else.

---

## The Elliptic Integrals

**Definition.** Let $k$ with $0 \leq k \leq 1$ be a **modulus**. The **complete elliptic integrals** of the first and second kind are

$$
K(k) = \int_0^{\pi/2} \frac{d\theta}{\sqrt{1 - k^2\sin^2\theta}} , \qquad
E(k) = \int_0^{\pi/2} \sqrt{1 - k^2\sin^2\theta}\, d\theta ,
$$

and the **incomplete** integrals are the same integrands integrated from $0$ to an arbitrary amplitude $\varphi$. The integral of the **third kind** is

$$
\Pi(n, k) = \int_0^{\pi/2} \frac{d\theta}{(1 - n\sin^2\theta)\sqrt{1 - k^2\sin^2\theta}} ,
$$

with a further parameter $n$; it is the integral that appears in the addition theorems for the incomplete integrals, and it is not used below.

**Theorem.** The complete integrals of the first and second kind converge for $0 \leq k < 1$. As $k \to 1^-$ the integral of the first kind diverges, $K(k) \to +\infty$, while the integral of the second kind has the finite limit $E(1) = 1$.

**Proof.** For $0 \leq k < 1$ the integrand of $K$ is continuous on the closed interval, hence bounded, and the integral is finite; the integrand is analytic in $k$ in a neighbourhood of the interval, so $K$ depends analytically on $k$, the derivative being obtained under the integral sign, as in *Analytic Functions and Power Series*, above. At $k = 1$ the integrand of $K$ is $1/\sqrt{1-\sin^2\theta} = 1/|\cos\theta|$, which behaves like $1/(\pi/2 - \theta)$ near the endpoint and is therefore not integrable on $(0,\pi/2)$; hence $K(k) \to +\infty$ as $k \to 1^-$. The integrand of $E$ at $k = 1$ is $|\cos\theta|$, whose integral over $(0,\pi/2)$ is $1$, and dominated convergence gives $E(k) \to 1$; the divergence of the first kind and the finiteness of the second are thus genuinely different. $\square$

**Remark.** The names are the classical ones. The integral of the first kind is the one inverted in the next section: its inverse with respect to the amplitude is the elliptic function $sn$, and the functions obtained by inverting the integrals are exactly the elliptic functions of the article, that is the doubly periodic meromorphic functions.

---

## The Jacobi Functions and the Weierstrass Function

**Definition.** Let $k$ be a modulus and let

$$
u = \int_0^{\varphi} \frac{d\theta}{\sqrt{1 - k^2\sin^2\theta}} .
$$

The **Jacobi elliptic functions** are $sn(u) = \sin\varphi$, $cn(u) = \cos\varphi$ and $dn(u) = \sqrt{1 - k^2\sin^2\varphi}$, the inverse of the integral of the first kind being taken as the definition of $\varphi$ as a function of $u$.

**Theorem.** The Jacobi functions are meromorphic and doubly periodic: $sn$ has periods $4K(k)$ and $2iK'(k)$, where $K'(k) = K(\sqrt{1-k^2})$, and

$$
sn^2u + cn^2u = 1 , \qquad dn^2u + k^2sn^2u = 1 , \qquad \frac{d}{du}sn\,u = cn\,u\,dn\,u .
$$

**Proof.** The relations follow from the definitions: $sn^2 + cn^2 = \sin^2\varphi + \cos^2\varphi = 1$ and $dn^2 + k^2 sn^2 = 1 - k^2\sin^2\varphi + k^2\sin^2\varphi = 1$, and the derivative is the chain rule applied to the inverse of the integral, $du/d\varphi = 1/\sqrt{1-k^2\sin^2\varphi}$. The double periodicity is the standard extension of $u$ to the complex plane by analytic continuation, with the periods computed from the integral: the continuation of the inverse of an integral of the first kind past the branch points produces the periods $4K$ and $2iK'$, and the standard argument is cited from the literature. $\square$

**Definition.** Let $\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$ be a lattice in $\mathbb{C}$, with $\operatorname{Im}(\omega_2/\omega_1) > 0$. The **Weierstrass elliptic function** is

$$
\wp(z) = \frac{1}{z^2} + \sum_{\omega \in \Lambda \setminus \{0\}} \left( \frac{1}{(z - \omega)^2} - \frac{1}{\omega^2} \right) .
$$

**Theorem.** The series defining $\wp$ converges normally on the complement of $\Lambda$, the function $\wp$ is meromorphic on $\mathbb{C}$ with a double pole at each lattice point and no other poles, it is even, and it is doubly periodic with period lattice $\Lambda$.

**Proof.** The convergence is standard: for $|\omega| > 2|z|$ the general term is bounded by $C|z|\,|\omega|^{-3}$ for a constant $C$, and the sum over the lattice of $|\omega|^{-3}$ converges; so the series converges normally on compact subsets of the complement of $\Lambda$, giving a meromorphic function by *Analytic Functions and Power Series*, above. The function is even because every term is even. For the periodicity, the derivative $\wp'(z) = -2\sum (z-\omega)^{-3}$ is manifestly periodic with period lattice $\Lambda$, and the function $\wp(z + \omega_i) - \wp(z)$ is therefore constant for each $i$; the constant is zero because $\wp$ is even, and the standard argument is cited from the literature. $\square$

**Theorem (the differential equation and the addition theorem).** With $g_2 = 60\sum' \omega^{-4}$ and $g_3 = 140\sum' \omega^{-6}$,

$$
\wp'(z)^2 = 4\wp(z)^3 - g_2\wp(z) - g_3 ,
$$

and for $u + v \notin \Lambda$,

$$
\wp(u+v) = -\wp(u) - \wp(v) + \frac{1}{4}\left( \frac{\wp'(u) - \wp'(v)}{\wp(u) - \wp(v)} \right)^2 .
$$

**Proof.** Both identities are the standard ones. The differential equation is obtained by comparing the Laurent expansions at the origin: the function $\wp'^2 - 4\wp^3 + g_2\wp + g_3$ is doubly periodic with poles only at the lattice points, and its expansion at the origin has no terms of nonnegative order, so it is holomorphic and periodic, hence constant, and the constant is zero because the expansion begins with a vanishing term. The addition theorem is proved by the same method: the function of $z$ obtained by subtracting the right-hand side from $\wp(z + v)$ is doubly periodic with at most a simple pole and no others, hence constant, and the constant is evaluated at a point where the terms are known. Both arguments are cited from the literature. $\square$

**Corollary.** The map $z \mapsto (\wp(z), \wp'(z))$ from $\mathbb{C}/\Lambda$ to the projective curve $Y^2Z = 4X^3 - g_2XZ^2 - g_3Z^3$ is a bijection of sets, and it carries the group law of $\mathbb{C}/\Lambda$ to the group law of the elliptic curve of *Elliptic Curves*, above.

**Proof.** The map is well defined on the torus by the periodicity, it is injective because $\wp$ determines $z$ up to sign and $\wp'$ determines the sign, and it is surjective because for each point of the curve the corresponding divisor of degree two on the torus is principal, by the standard argument of the theory; the group law is the statement that the inverse is a group homomorphism, and it is the analytic content of the algebra of *Elliptic Curves*, above. The details are cited from the literature. $\square$

---

## Lattices, the Modular Parameter and Theta Functions

**Theorem.** Two lattices $\Lambda$ and $\Lambda'$ give isomorphic complex tori exactly when they are homothetic, that is $\Lambda' = \lambda\Lambda$ for some $\lambda \in \mathbb{C}^{\times}$; every lattice is homothetic to one of the form $\mathbb{Z} + \mathbb{Z}\tau$ with $\tau$ in the upper half-plane, and the classes of lattices are parametrised by the orbit space of the upper half-plane under the action of $SL(2,\mathbb{Z})$.

**Proof.** A biholomorphism of $\mathbb{C}/\Lambda$ onto $\mathbb{C}/\Lambda'$ lifts to an automorphism of $\mathbb{C}$ as a group, which is multiplication by a nonzero complex number, and it carries $\Lambda$ to $\Lambda'$; conversely a homothety gives an isomorphism of tori. Given a lattice with basis $(\omega_1, \omega_2)$ one rescales by $\omega_1^{-1}$ to reach $\mathbb{Z} + \mathbb{Z}\tau$ with $\tau = \omega_2/\omega_1$ in the upper half-plane after possibly exchanging the basis, and two such lattices are homothetic exactly when the corresponding $\tau$ are related by a matrix of $SL(2,\mathbb{Z})$ acting by fractional linear transformations. That action and the elliptic curves attached to the resulting tori are the subject of *Modular Forms*, below in this Part, where the modular functions are developed; this article uses only the parametrisation. $\square$

**Definition.** The **modular function** is $j(\tau) = 1728\,g_2^3/(g_2^3 - 27g_3^2)$, evaluated on $\mathbb{Z} + \mathbb{Z}\tau$; it is invariant under the action of $SL(2,\mathbb{Z})$ and it separates the orbits, so that the classes of lattices are the values of $j$.

**Theorem (the complete integrals, the arithmetic–geometric mean and the theta functions).** Let $M(a,b)$ be the arithmetic–geometric mean of $a, b > 0$. Then for $0 \leq k < 1$,

$$
K(k) = \frac{\pi}{2M(1, \sqrt{1-k^2})} ,
$$

and the Jacobi functions are the quotients of the theta functions

$$
\vartheta_1, \vartheta_2, \vartheta_3, \vartheta_4 ,
$$

which are entire functions of a variable and a parameter, with product expansions and the quasi-periodicity of the theory; the evaluation

$$
K(1/\sqrt2) = \frac{\Gamma(1/4)^2}{4\sqrt\pi} ,
\qquad
\int_0^1 K(k)\,dk = 2G ,
$$

where $G$ denotes **Catalan's constant** $G = \beta(2) = \sum_{n \geq 0} (-1)^n(2n+1)^{-2}$, with $\beta$ the Dirichlet beta function, are the classical evaluations of the integral of the first kind.

**Proof.** The formula for $K$ in terms of the arithmetic–geometric mean is Gauss's: the mean is computed by the iteration $a_{n+1} = (a_n + b_n)/2$, $b_{n+1} = \sqrt{a_nb_n}$, and the identity $K(k) = \pi/(2M(1,\sqrt{1-k^2}))$ follows by the standard substitution of the theory, cited from the literature. The product expansions of the theta functions and the expression of the Jacobi functions as their quotients are likewise standard and cited. The evaluation at $k = 1/\sqrt2$ is the classical evaluation in terms of the Gamma function, and the identity $\int_0^1K(k)\,dk = 2G$ is the standard evaluation of $\int_0^{\pi/2}\theta/\sin\theta\,d\theta$, obtained from the definition of $K$ by exchanging the two integrations; both evaluations are cited from the literature. $\square$

**Remark.** The constant $G$ of Catalan appears above only inside that display and in the sentence that defines it; the letter is a group symbol everywhere else in the corpus, and inside this article it is confined to the paragraph that defines it, as the shared conventions require. The Dirichlet beta function satisfies $\beta(2) = G$ and $\beta(s)$ is the alternating analogue of the zeta function of *Zeta Functions*, later in this Part.

---

## Summary

The elliptic integrals of the first and second kind, $K$ and $E$, converge for a modulus $k < 1$ and diverge at $k = 1$; inverting the integral of the first kind gives the Jacobi elliptic functions $sn$, $cn$, $dn$, which are meromorphic and doubly periodic, with periods $4K$ and $2iK'$ and the relations $sn^2 + cn^2 = 1$ and $dn^2 + k^2sn^2 = 1$. The Weierstrass function $\wp$ attached to a lattice $\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$ is meromorphic with a double pole at every lattice point, even and doubly periodic, and satisfies the differential equation $\wp'^2 = 4\wp^3 - g_2\wp - g_3$ and the addition theorem; the map $z \mapsto (\wp(z), \wp'(z))$ identifies the complex torus $\mathbb{C}/\Lambda$ with the elliptic curve of *Elliptic Curves*, and it carries the group law of the torus to the algebraic group law. Lattices are classified up to homothety by the modular parameter $\tau$ in the upper half-plane modulo $SL(2,\mathbb{Z})$, with the modular function $j$ separating the classes; the complete integral is computed by the arithmetic–geometric mean, the Jacobi functions are quotients of theta functions, and the classical evaluations include $K(1/\sqrt2) = \Gamma(1/4)^2/(4\sqrt\pi)$ and $\int_0^1K(k)\,dk = 2G$ with $G$ Catalan's constant. The modular forms are *Modular Forms*, below in this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $K(k)$, $E(k)$ | The modulus, and the complete elliptic integrals of the first and second kind |
| $sn$, $cn$, $dn$ | The Jacobi elliptic functions |
| $K'(k) = K(\sqrt{1-k^2})$ | The complementary complete integral |
| $\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$ | A period lattice, with $\operatorname{Im}(\omega_2/\omega_1) > 0$ |
| $\wp$ | The Weierstrass elliptic function, `\wp` and never a plain $p$ |
| $g_2$, $g_3$ | The invariants of the lattice, the coefficients of the differential equation |
| $\mathbb{C}/\Lambda$ | The complex torus of the lattice |
| $\tau$ | The modular parameter in the upper half-plane |
| $j(\tau)$ | The modular function, separating the classes of lattices |
| $M(a,b)$ | The arithmetic–geometric mean |
| $\vartheta_1, \vartheta_2, \vartheta_3, \vartheta_4$ | The theta functions |
| $G$ | **Catalan's constant** in this article only, $G = \beta(2)$ |
| $\beta(s)$ | The Dirichlet beta function, with $\beta(2) = G$ |

## Further Reading

- J. M. Borwein and P. B. Borwein, *Pi and the AGM* (Wiley, 1987), for the arithmetic–geometric mean, the complete elliptic integrals and their evaluations.
- K. Chandrasekharan, *Elliptic Functions* (Springer, 1985), for the theta functions, the Jacobi and Weierstrass functions and the periodicity arguments.
- D. Mumford, *Tata Lectures on Theta I* (Birkhäuser, 1983), for the theta functions and their product expansions.
- J. Stillwell, *Mathematics and Its History* (Springer, 3rd ed. 2010), for the classical evaluations, including the integral of $K$ and the role of Catalan's constant.
- E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis* (Cambridge University Press, 4th ed. 1927), for the standard treatment of the elliptic integrals and functions and the addition theorem.

