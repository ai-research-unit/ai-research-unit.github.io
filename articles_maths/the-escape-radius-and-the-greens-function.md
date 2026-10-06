# __The Escape Radius and the Green's Function__

## Introduction

The basin of infinity of a polynomial is the set of points whose iterates tend to $\infty$, and on it the dynamics is linearised by a single harmonic function: the **Green's function**, the function $G$ that measures the rate of escape. This article defines $G$, proves its existence as the limit of the normalised logarithms of the iterates, records the functional equation $G(f(z)) = d\,G(z)$ that makes it the eigenfunction of the pull-back by $f$, computes the explicit series for the quadratic family, and identifies the Laplacian of $G$ with the invariant measure of the Julia set. The **escape radius** is the companion object: the radius beyond which the escape is certain, so that the escape-time algorithm of *The Mandelbrot Set and the Quadratic Family* terminates. The article closes with the potential-theoretic reading of $G$, in which it is the equilibrium potential of the filled Julia set.

The article depends on *The Julia Sets of a Complex Polynomial* for the partition and the filled Julia set, and on *The Mandelbrot Set and the Quadratic Family* for the escape-time algorithm. The Böttcher coordinate, the external rays and the landing theorems are Part IV's, and are named here only where the Green's function is their modulus; the equilibrium measure and the logarithmic potential are those of *Potential Theory* of Part III, and the invariant measure of the Julia set is that of *The Julia Sets of a Complex Polynomial*. The dimension of the Julia set is the following article's. No physics is invoked.

## The Escape Radius

**Definition.** Let $f(z) = a_d z^d + \cdots + a_0$ be a polynomial of degree $d \geq 2$. A number $R$ is an **escape radius** for $f$ if $|z| > R$ implies $|f(z)| > |z|$; the **escape locus** is then $\{z : |z| > R\}$, and a point of the escape locus has an orbit diverging to $\infty$.

**Theorem (the crude radius).** Let

$$
R = 1 + |a_{d-1}| + \cdots + |a_0| .
$$

Then $R$ is an escape radius for $f$: for $|z| > R$ one has $|f(z)| > |z|$, and consequently $f^n(z) \to \infty$. In particular the filled Julia set and the Julia set are contained in the closed disk of radius $R$.

**Proof.** For $|z| > R > 1$,

$$
|f(z)| \geq |z|^d - \sum_{k=0}^{d-1}|a_k|\,|z|^k \geq |z|^d - \Bigl(\sum_{k=0}^{d-1}|a_k|\Bigr)|z|^{d-1} = |z|^{d-1}\bigl(|z| - (R-1)\bigr) > |z|^{d-1} \geq |z| ,
$$

since $|z| - (R-1) > 1$ and $|z|^{d-1} \geq |z|$ for $|z| > 1$ and $d \geq 2$. Hence the moduli increase and diverge.

**Theorem (the optimal radius for the quadratic family).** For $f_c(z) = z^2+c$ the number

$$
R(c) = \frac{1 + \sqrt{1+4|c|}}{2}
$$

is the least escape radius; it is the positive root of $x^2 - x - |c| = 0$, and

$$
|z| > R(c) \implies |f_c(z)| \geq |z|^2-|c| > |z|, \qquad \frac{|f_c(z)|}{R(c)} \geq \Bigl(\frac{|z|}{R(c)}\Bigr)^{2} ,
$$

using $R(c)^2 = R(c)+|c|$; so the moduli increase and their ratios to $R(c)$ at least square at each step, whence the orbit diverges.

In particular $R(c) \leq 2$ exactly when $|c| \leq 2$, so the round number $2$ is an escape radius for every parameter in the closed disk of radius $2$, which is the disk containing $M$.

**Proof.** $|z^2+c| \geq |z|^2 - |c|$; this exceeds $|z|$ exactly when $|z|^2 - |z| - |c| > 0$, that is when $|z| > R(c)$. The radius is the least one valid for all the parameters of modulus $|c|$: for the real parameter $c = -|c|$ the filled Julia set is the real interval ending at the repelling fixed point $R(c)$, so for every $R' < R(c)$ there are non-escaping points of modulus greater than $R'$.

**Example.** $R(0) = 1$, the escape radius of $z^2$; $R(-1) = R(i) = (1+\sqrt5)/2 = 1.618034\ldots$; $R(-2) = R(2) = 2$. The values were recomputed from the formula.

**Corollary (termination of the algorithm).** The escape-time algorithm of *The Mandelbrot Set and the Quadratic Family* may stop at the first $n$ with $|f_c^n(0)| > 2$: once the orbit leaves the disk of radius $2$, it escapes, so the escape time $n(c)$ is finite for every $c \notin M$, and it is bounded by the escape time of the initial value when $|c| > 2$.

## The Green's Function

### Definition and Existence

**Theorem (existence).** Let $f$ be a polynomial of degree $d \geq 2$. For every $z$ the limit

$$
G(z) = \lim_{n \to \infty} \frac{1}{d^n} \log^+\bigl|f^n(z)\bigr| , \qquad \log^+ t = \max(\log t, 0),
$$

exists and is finite. The function $G$ so defined is the **Green's function of the basin of infinity**.

**Proof sketch.** Choose an escape radius $R$. If $|z| > R$ then $|f^n(z)|$ increases without bound, and the difference $\log|f^{n+1}(z)| - d\log|f^n(z)|$ tends to $0$ at a geometric rate, because $f$ is asymptotically $z \mapsto a_d z^d$ at infinity: the sequence $\log|f^n(z)|/d^n$ is Cauchy. For a general $z$ one chooses $N$ with $|f^N(z)| > R$, which exists for $z$ outside $K$ and is impossible for $z \in K$; the tail of the sequence is controlled by the first estimate, and the contribution before $N$ is killed by the factor $d^{-n}$. For $z \in K$ the iterates are bounded, so $\log^+|f^n(z)| = 0$ for large $n$ and $G(z) = 0$. The uniform convergence on compact subsets off $K$ gives the continuity and the harmonicity proved below.

**Theorem (basic properties).** The Green's function has the following properties.

**(a)** $G \geq 0$, and $G(z) = 0$ exactly on the filled Julia set $K(f)$.

**(b)** $G$ is continuous on $\mathbb{C}$ and harmonic on the basin of infinity $A(\infty) = \mathbb{C} \setminus K(f)$.

**(c)** $G(f(z)) = d\, G(z)$ for every $z$.

**(d)** $G(z) = \log|z| + o(1)$ as $z \to \infty$; more precisely $G - \log|z|$ is harmonic near $\infty$ and bounded, so it extends harmonically across $\infty$ and has limit $0$ there.

**Proof.** (a) is clear from the definition and the escape criterion. (c) follows from $\log^+|f^{n+1}(z)| = \log^+|f^n(f(z))|$ and the definition applied to $f(z)$. (b) and (d): the limit is locally uniform off $K$, and each $\log^+|f^n|/d^n$ is harmonic where $f^n \neq 0$; since $d^{-n}\log|f^n(z)| = \log|z| + O(1/|z|^d)$ for large $z$, the normalisation makes the limit tangent to $\log|z|$.

**Corollary.** The Böttcher coordinate of *The Fatou Components and the Classification of the Dynamics* is $\varphi = \exp(G + iH)$, where $H$ is a harmonic conjugate of $G$ on the basin; it satisfies $\varphi(f(z)) = \varphi(z)^d$ and $\varphi(z) = z + O(1)$ at infinity, and $|\varphi| = e^{G}$. The level curves of $G$ are the **equipotentials** of the basin and the level curves of $H$ are the **external rays**; the rays and their landing are Part IV's.

### The Explicit Series for the Quadratic Family

**Theorem.** For $f_c(z) = z^2+c$ and $z$ outside the filled Julia set,

$$
G(z) = \log|z| + \sum_{n=0}^{\infty} \frac{1}{2^{n+1}} \log\left| 1 + \frac{c}{f_c^n(z)^2} \right| ,
$$

the series converging because $|f_c^n(z)| \to \infty$.

**Proof.** Write $\log|f_c(w)| = 2\log|w| + \log|1 + c/w^2|$ and iterate: after $n$ steps,

$$
\frac{1}{2^n}\log|f_c^n(z)| = \log|z| + \sum_{k=0}^{n-1}\frac{1}{2^{k+1}}\log\left|1 + \frac{c}{f_c^k(z)^2}\right| .
$$

Letting $n \to \infty$ gives the display: the left-hand side tends to $G(z)$, by the definition of $G$ as the limit $\lim_n 2^{-n}\log|f_c^n(z)|$, and the series on the right converges because $|f_c^n(z)| \to \infty$ makes its terms decay geometrically.

**Remark (the binomial expansion).** The series is the normalised sum of the binomial expansions of the squaring steps: each step factors as $w^2+c = w^2(1+c/w^2)$, so that $f_c^{k+1}(z) = f_c^k(z)^2\bigl(1+c/f_c^k(z)^2\bigr)$, and taking logarithms gives the recurrence

$$
\log\bigl|f_c^{k+1}(z)\bigr| - 2\log\bigl|f_c^k(z)\bigr| = \log\left|1+\frac{c}{f_c^k(z)^2}\right| ,
$$

whose weighted sum $2^{-(k+1)}$ over $k$ and normalisation by $2^n$ produce the displayed series. It is the asymptotic development of $G$ at infinity, $G(z) = \log|z| + O(1/|z|^2)$.

**Example (numerical check).** The series and the normalised-logarithm definition agree to double precision. For $c = 0$ and $z = 3$ both give $G = \log 3 = 1.0986122887$; for $c = -1$ and $z = 3$ both give $G = 1.0357521796$; for $c = 0.3+0.5i$ and $z = 3$ both give $G = 1.1167511353$. On the filled Julia set, $G = 0$ at the tested points, for instance $G = 0$ at $z = 0.5$ for $c = 0$, at $z = 0$ for $c = -1$, at $z = 0.5$ for $c = 1/4$, and at $z = 0$ for $c = -2$.

**Example (capacity one).** The difference $G(z) - \log|z|$ decays like $|z|^{-2}$ along the positive real axis: it is $-5.051 \times 10^{-3}$ at $|z| = 10$, $-5.001 \times 10^{-5}$ at $|z| = 100$, and $-5.000 \times 10^{-9}$ at $|z| = 10^4$ for $c = -1$. The limit of $G - \log|z|$ at infinity is therefore $0$, which says that the filled Julia set has **logarithmic capacity** one.

## The Laplacian and the Invariant Measure

**Theorem.** Let $\mu$ be the equilibrium measure of the filled Julia set, that is, the unique probability measure of minimal energy in the logarithmic kernel of *Potential Theory*. Then

$$
G(z) = \int \log|z - w| \, d\mu(w) , \qquad z \in \mathbb{C},
$$

the logarithmic potential of $\mu$; the function $G$ is the unique harmonic function on $A(\infty)$ that vanishes on $\partial A(\infty) = J(f)$ and is tangent to $\log|z|$ at infinity; and

$$
\mu = \frac{1}{2\pi}\,\Delta G
$$

in the sense of distributions, where $\Delta$ is the Laplace operator. The measure $\mu$ is exactly the Brolin measure of maximal entropy of *The Julia Sets of a Complex Polynomial*, supported on $J(f)$ and invariant under $f$.

**Proof sketch.** The equilibrium measure of a compact set of capacity $1$ minimises the energy $\iint \log\frac{1}{|z-w|}d\nu(z)d\nu(w)$; its potential $U^\nu(z) = \int\log|z-w|d\nu$ equals the Robin constant $0$ on the set and is the largest harmonic minorant of $\log|z|$ type, which is the defining property of the Green's function. Hence $G = U^\mu$ and $\Delta G/2\pi = \mu$, because the distributional Laplacian of the logarithmic kernel is $2\pi$ times the Dirac mass. The identification with the Brolin measure follows because both are the equilibrium measure of the Julia set, and the invariance $f_*\mu = \mu$ is the invariance $G \circ f = dG$ together with the uniqueness of the equilibrium measure. The energy and the equilibrium measure are those of *Potential Theory*; the invariance and the identification with the maximal-entropy measure are those of *The Julia Sets of a Complex Polynomial*.

**Corollary.** The escape rate of a point is the logarithmic potential of the equilibrium measure at that point, and the capacity of the filled Julia set is $1$ for every monic polynomial, since the Green's function is tangent to $\log|z|$ at infinity.

**Remark.** The measure $\mu$ is the harmonic measure of the basin of infinity evaluated on the Julia set, and it is the measure obtained as the weak limit of the normalised counting measures of the preimages of any non-exceptional point; the two descriptions are the same equilibrium measure, seen from the basin and from the dynamics. The equilibrium measure of the whole Julia set is thus computed by the single harmonic function $G$, and the fractal theory of the Julia set begins from this function and its level curves.

## Summary

The escape radius of a polynomial of degree $d \geq 2$ is any $R$ with $|z| > R \Rightarrow |f(z)| > |z|$; the value $R = 1 + \sum|a_k|$ always works, and for the quadratic family the least value is $R(c) = \tfrac12(1+\sqrt{1+4|c|})$, which is at most $2$ exactly for $|c| \leq 2$. The escape radius makes the escape-time algorithm of the parameter theory terminate.

The Green's function $G(z) = \lim d^{-n}\log^+|f^n(z)|$ exists, is continuous, vanishes exactly on the filled Julia set, is harmonic on the basin of infinity, satisfies $G \circ f = dG$, and is tangent to $\log|z|$ at infinity. For the quadratic family it has the explicit series $\log|z| + \sum 2^{-(n+1)}\log|1+c/f^n(z)^2|$. Its modulus is the Böttcher coordinate and its level curves are the equipotentials; its Laplacian, normalised by $2\pi$, is the equilibrium measure of the filled Julia set, which is the Brolin measure of maximal entropy, and the capacity of the filled Julia set is $1$. The potential theory is that of *Potential Theory* of Part III; the external rays and the landing theorems are Part IV's; the dimension of the Julia set is the subject of the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $R(c)$ | Escape radius; least escape radius $\tfrac12(1+\sqrt{1+4\lvert c\rvert})$ of the quadratic family |
| $n(c)$ | Escape time of the parameter $c$, from *The Mandelbrot Set and the Quadratic Family* |
| $G$ | Green's function of the basin of infinity |
| $\log^+ t$ | $\max(\log t, 0)$ |
| $\varphi = e^{G+iH}$ | Böttcher coordinate, $\lvert\varphi\rvert = e^{G}$ |
| equipotential, external ray | Level curve of $G$; level curve of the harmonic conjugate $H$ |
| $\mu = \Delta G/2\pi$ | Equilibrium measure of $K$, the Brolin measure |
| capacity | $\exp(\lim(G-\log\lvert z\rvert)) = 1$ for a monic polynomial |
| $U^\mu(z) = \int\log\lvert z-w\rvert d\mu(w)$ | Logarithmic potential, equal to $G$ |

## Further Reading

- Ludwig Bieberbach, *Lehrbuch der Funktionentheorie*, volume 2 (Teubner, 1927), for the escape radius and the first use of the Green's function in iteration.
- Hans Brolin, "Invariant sets under iteration of rational functions", *Arkiv för Matematik* 6 (1965), 103–144, for the equilibrium measure and the Green's function.
- Thomas Ransford, *Potential Theory in the Complex Plane* (Cambridge University Press, 1995), for the logarithmic kernel, the capacity and the equilibrium measure.
- Norbert Steinmetz, *Rational Iteration* (de Gruyter, 1993), for the Green's function, the explicit expansions and the Böttcher coordinate.
- John Milnor, *Dynamics in One Complex Variable*, 3rd edition (Princeton University Press, 2006), for the equipotentials, the external rays and the Böttcher coordinate.
- Lennart Carleson and Theodore W. Gamelin, *Complex Dynamics* (Springer, 1993), for the escape radius and the landing of the rays.
