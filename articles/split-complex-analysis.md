
# Split Complex Analysis

## Introduction

This article introduces split complex analysis as the study of differentiable functions of a split complex variable. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The split complex algebra is assumed from the article on split complex algebra, and the idempotent decomposition is used throughout. No physics is invoked. The hyperbolic structure that replaces the circular structure of complex analysis is developed systematically.

## The Split Complex Plane

### Points and Distance

A split complex number is written

$$
z = x + j y, \qquad x, y \in \mathbb{R},
$$

where $j^2 = +1$. The real number $x$ is the **real part**, and $y$ is the **imaginary part**. We write $x = \operatorname{Re} z$ and $y = \operatorname{Im} z$.

The **Euclidean modulus** of $z$ is

$$
\|z\|_E = \sqrt{x^2 + y^2},
$$

and the **Euclidean distance** between two split complex numbers $z$ and $w$ is

$$
d(z, w) = \|z - w\|_E.
$$

This makes $\mathbb{D}$ a metric space isometric to $\mathbb{R}^2$. The Euclidean modulus satisfies the triangle inequality and is positive-definite, so it is a genuine norm.

The **split modulus** is

$$
|z| = \sqrt{|x^2 - y^2|},
$$

which is not a norm. It vanishes on the light cone $x = \pm y$, and it is indefinite. It is used in the study of the multiplicative structure, not the topological structure.

### Balls and Neighborhoods

The **open ball** of radius $r > 0$ centered at $z_0$ is

$$
B(z_0, r) = \{z \in \mathbb{D} : \|z - z_0\|_E < r\}.
$$

It is an open disk in the split complex plane, exactly as in the complex plane. The topology of $\mathbb{D}$ is the ordinary Euclidean topology of $\mathbb{R}^2$.

### Open and Closed Sets

A set $U \subseteq \mathbb{D}$ is **open** if for every $z_0 \in U$ there exists $r > 0$ with $B(z_0, r) \subseteq U$.

A set $F \subseteq \mathbb{D}$ is **closed** if its complement $\mathbb{D} \setminus F$ is open.

Arbitrary unions of open sets are open. Finite intersections of open sets are open. Dually for closed sets.

### Connectedness and Domains

A set $U \subseteq \mathbb{D}$ is **connected** if it cannot be written as the disjoint union of two non-empty open sets. It is **path-connected** if any two points can be joined by a continuous path in $U$. For open subsets of $\mathbb{D}$, connectedness and path-connectedness are equivalent.

A **domain** is a non-empty open connected subset of $\mathbb{D}$. Domains are the natural setting for split complex analysis, because differentiability on a domain imposes constraints that are weaker than in the complex case but still nontrivial.

### Compactness

A set $K \subseteq \mathbb{D}$ is **compact** if every open cover of $K$ has a finite subcover.

**Theorem (Heine–Borel).** A subset of $\mathbb{D}$ is compact iff it is closed and bounded in the Euclidean norm.

**Theorem.** A continuous split-complex-valued function on a compact set is bounded and attains its maximum and minimum Euclidean modulus.

## Limits and Continuity

### Limits of Sequences

A sequence $(z_n)$ of split complex numbers **converges** to $L \in \mathbb{D}$ if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
n \geq N \implies \|z_n - L\|_E < \epsilon.
$$

We write $z_n \to L$ or $\lim_{n \to \infty} z_n = L$.

**Uniqueness.** If $z_n \to L$ and $z_n \to L'$, then $L = L'$.

**Componentwise convergence.** Write $z_n = x_n + j y_n$ and $L = a + j b$. Then

$$
z_n \to L \iff x_n \to a \text{ and } y_n \to b.
$$

This is the reason split complex convergence is no harder than real convergence: it is two real convergences in parallel.

**Boundedness.** Every convergent sequence is bounded. The converse fails.

**Algebra of limits.** If $z_n \to L$ and $w_n \to M$, then

$$
z_n + w_n \to L + M, \qquad z_n w_n \to L M.
$$

There is no quotient rule in general, because $\mathbb{D}$ has zero divisors.

### Cauchy Sequences

A sequence $(z_n)$ is **Cauchy** if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
m, n \geq N \implies \|z_m - z_n\|_E < \epsilon.
$$

**Theorem.** In $\mathbb{D}$, a sequence converges iff it is Cauchy. This is the completeness of $\mathbb{D}$ as a metric space, and it follows from the completeness of $\mathbb{R}$ applied to the real and imaginary parts.

### Limits of Functions

Let $f : D \to \mathbb{D}$ with $D \subseteq \mathbb{D}$, and let $z_0$ be a limit point of $D$. We say

$$
\lim_{z \to z_0} f(z) = L
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z \in D, \; 0 < \|z - z_0\|_E < \delta \implies \|f(z) - L\|_E < \epsilon.
$$

**Uniqueness.** If the limit exists, it is unique.

**Sequential criterion.** $\lim_{z \to z_0} f(z) = L$ iff for every sequence $(z_n)$ in $D \setminus \{z_0\}$ with $z_n \to z_0$, we have $f(z_n) \to L$.

**Algebra of limits.** Sums and products of limits are the limits of the sums and products.

### Continuity

A function $f : D \to \mathbb{D}$ is **continuous at** $z_0 \in D$ if

$$
\lim_{z \to z_0} f(z) = f(z_0).
$$

Equivalently, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z \in D, \; \|z - z_0\|_E < \delta \implies \|f(z) - f(z_0)\|_E < \epsilon.
$$

$f$ is **continuous on** $D$ if it is continuous at every point of $D$.

**Theorem.** Sums and products of continuous functions are continuous. Compositions of continuous functions are continuous.

**Theorem.** $f$ is continuous iff the preimage of every open set is open. Equivalently, the preimage of every closed set is closed.

**Componentwise continuity.** Write $f(z) = u(x, y) + j v(x, y)$. Then $f$ is continuous at $z_0 = x_0 + j y_0$ iff $u$ and $v$ are continuous at $(x_0, y_0)$. This reduces split complex continuity to real continuity of two functions of two variables.

### Uniform Continuity

A function $f : D \to \mathbb{D}$ is **uniformly continuous** if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z, w \in D, \; \|z - w\|_E < \delta \implies \|f(z) - f(w)\|_E < \epsilon.
$$

**Theorem.** A continuous function on a compact set is uniformly continuous.

## Split Complex Differentiability

### The Derivative

Let $f : U \to \mathbb{D}$ with $U$ open, and let $z_0 \in U$. The **derivative** of $f$ at $z_0$ is

$$
f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h},
$$

provided the limit exists. If it does, $f$ is **split complex differentiable** at $z_0$, or **holomorphic** at $z_0$ in the split sense.

The limit is taken in the split complex plane, so $h$ can approach $0$ from any direction. But because $\mathbb{D}$ has zero divisors, the quotient is not always defined, and the limit must be taken along paths where $h$ is invertible. This is the fundamental difference from the complex case.

**Theorem.** Split complex differentiability implies continuity. The converse fails.

### The Cauchy–Riemann Equations

Write $f(z) = u(x, y) + j v(x, y)$, where $z = x + jy$ and $u, v : U \to \mathbb{R}$.

**Theorem.** $f$ is split complex differentiable at $z_0 = x_0 + j y_0$ iff $u$ and $v$ are real differentiable at $(x_0, y_0)$ and satisfy the **split Cauchy–Riemann equations**

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = \frac{\partial v}{\partial x}.
$$

**Proof.** Write $h = h_1 + j h_2$. The difference quotient is

$$
\frac{f(z_0 + h) - f(z_0)}{h} = \frac{(u_x h_1 + u_y h_2) + j (v_x h_1 + v_y h_2)}{h_1 + j h_2} + o(1).
$$

For the limit to exist independently of the direction of $h$, the numerator must be a split complex multiple of $h$. This forces the split Cauchy–Riemann equations. $\square$

**Corollary.** If $f$ is split complex differentiable, then $u$ and $v$ satisfy the **wave equation**:

$$
\frac{\partial^2 u}{\partial x^2} - \frac{\partial^2 u}{\partial y^2} = 0, \qquad \frac{\partial^2 v}{\partial x^2} - \frac{\partial^2 v}{\partial y^2} = 0.
$$

**Proof.** Differentiate the split Cauchy–Riemann equations and use the equality of mixed partials. $\square$

This is the fundamental difference from complex analysis: the real and imaginary parts of a holomorphic function are harmonic in the complex case, and solutions of the wave equation in the split complex case. The change of sign in the Cauchy–Riemann equations changes the Laplacian into the d'Alembertian.

### The Wirtinger Derivatives

Define the **split Wirtinger derivatives**

$$
\frac{\partial}{\partial z} = \frac{1}{2}\left( \frac{\partial}{\partial x} + j \frac{\partial}{\partial y} \right), \qquad \frac{\partial}{\partial \bar{z}} = \frac{1}{2}\left( \frac{\partial}{\partial x} - j \frac{\partial}{\partial y} \right).
$$

**Theorem.** $f$ is split complex differentiable iff $\partial f / \partial \bar{z} = 0$. In that case,

$$
f'(z) = \frac{\partial f}{\partial z}.
$$

The condition $\partial f / \partial \bar{z} = 0$ is the split Cauchy–Riemann equations in compact form.

### Rules of Differentiation

**Linearity.** $(af + bg)' = a f' + b g'$.

**Product rule.** $(fg)' = f' g + f g'$.

**Quotient rule.** $(f/g)' = (f' g - f g')/g^2$ where $g$ is invertible.

**Chain rule.** $(f \circ g)'(z) = f'(g(z)) g'(z)$.

**Inverse function rule.** If $f$ is split complex differentiable at $z_0$ with $f'(z_0)$ invertible and $f^{-1}$ is defined near $f(z_0)$, then

$$
(f^{-1})'(f(z_0)) = \frac{1}{f'(z_0)}.
$$

## The Idempotent Decomposition

### Definition

The **idempotents** of $\mathbb{D}$ are

$$
e_+ = \frac{1 + j}{2}, \qquad e_- = \frac{1 - j}{2}.
$$

They satisfy $e_+^2 = e_+$, $e_-^2 = e_-$, $e_+ e_- = 0$, and $e_+ + e_- = 1$.

Every split complex number decomposes uniquely as

$$
z = z_+ e_+ + z_- e_-, \qquad z_+ = x + y, \quad z_- = x - y.
$$

### Differentiability in the Idempotent Basis

Write $f(z) = f_+(z) e_+ + f_-(z) e_-$, where $f_+$ and $f_-$ are real-valued functions. Then

$$
f \text{ is split complex differentiable} \iff f_+ \text{ is differentiable in } z_+ \text{ and } f_- \text{ is differentiable in } z_-.
$$

**Proof.** In the idempotent basis, the split complex algebra is $\mathbb{R} \oplus \mathbb{R}$, and the multiplication is componentwise. So a function $f$ is differentiable iff each component is differentiable with respect to its own variable. $\square$

This is the **fundamental theorem of split complex analysis**: differentiability in $\mathbb{D}$ is equivalent to differentiability in each of the two real components separately. There is no interaction between the two components, because the idempotents annihilate each other.

### Consequences

**No conformality.** Split complex differentiable functions do not preserve angles in general, because the two components can scale differently.

**No Cauchy integral formula.** There is no single integral formula that reconstructs a split complex differentiable function from its boundary values, because the two components are independent.

**No Liouville theorem.** A bounded split complex differentiable function on all of $\mathbb{D}$ need not be constant, because each component can be an arbitrary bounded differentiable function of one real variable.

## Integration

### Contour Integrals

Let $\gamma : [a, b] \to \mathbb{D}$ be a piecewise continuously differentiable path, and let $f$ be continuous on the image of $\gamma$. The **contour integral** of $f$ along $\gamma$ is

$$
\int_\gamma f(z) \, dz = \int_a^b f(\gamma(t)) \gamma'(t) \, dt.
$$

**Linearity.** $\int_\gamma (af + bg) = a \int_\gamma f + b \int_\gamma g$.

**Reversal.** $\int_{-\gamma} f = -\int_\gamma f$.

**Additivity.** If $\gamma$ is the concatenation of $\gamma_1$ and $\gamma_2$, then $\int_\gamma f = \int_{\gamma_1} f + \int_{\gamma_2} f$.

**Estimation.** If $\|f(z)\|_E \leq M$ on $\gamma$ and $L$ is the length of $\gamma$, then

$$
\left\| \int_\gamma f(z) \, dz \right\|_E \leq M L.
$$

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat, split version).** If $f$ is split complex differentiable on a simply connected domain $U$ and $\gamma$ is a closed contour in $U$, then

$$
\oint_\gamma f(z) \, dz = 0
$$

provided the contour does not cross the light cone.

**Proof.** In the idempotent basis, the integral decomposes into two real integrals, one for each component. Each component is a real line integral of a differentiable function of one variable, and each vanishes on a closed contour. $\square$

**Caution.** The theorem fails if the contour crosses the light cone, because the idempotent components are not defined there in a single-valued way. The light cone is the analogue of the branch cut in complex analysis, and it must be avoided.

### The Cauchy Integral Formula

There is **no** general Cauchy integral formula in split complex analysis. The reason is that the kernel $1/(w - z)$ has a singularity on the light cone, and the integral around a point depends on the path in a way that cannot be removed by a single formula.

However, if the function is written in the idempotent basis, each component has its own Cauchy integral formula:

$$
f_+(z_+) = \frac{1}{2\pi i} \oint \frac{f_+(\zeta_+)}{\zeta_+ - z_+} \, d\zeta_+,
$$

and similarly for $f_-$. But these are complex formulas applied to real functions, and they require complexification of the components. They are not split complex formulas.

## Power Series

### Definition

A **power series** centered at $z_0$ is

$$
\sum_{n=0}^\infty c_n (z - z_0)^n, \qquad c_n \in \mathbb{D}.
$$

The **radius of convergence** is

$$
R = \frac{1}{\limsup_{n \to \infty} \|c_n\|_E^{1/n}},
$$

with the conventions $R = 0$ if the limsup is $\infty$ and $R = \infty$ if the limsup is $0$.

**Theorem.** The series converges absolutely for $\|z - z_0\|_E < R$ and diverges for $\|z - z_0\|_E > R$. On $\|z - z_0\|_E < R$ it converges uniformly on compact subsets.

**Theorem.** A power series is split complex differentiable on $\|z - z_0\|_E < R$, and its derivative is obtained by term-by-term differentiation:

$$
\frac{d}{dz} \sum_{n=0}^\infty c_n (z - z_0)^n = \sum_{n=1}^\infty n c_n (z - z_0)^{n-1}.
$$

The differentiated series has the same radius of convergence.

### Taylor Series

**Theorem (Taylor, split version).** If $f$ is split complex differentiable on a domain containing the closed disk $\overline{B}(z_0, r)$, then $f$ has a power series expansion

$$
f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n
$$

valid for $\|z - z_0\|_E < r$.

**Proof.** In the idempotent basis, each component has a real Taylor expansion, and the two expansions combine. $\square$

**Corollary.** A split complex differentiable function is analytic: it equals its Taylor series in a neighborhood of every point.

**Caution.** The identity theorem fails in general, because a split complex differentiable function can vanish on a set with an accumulation point without being identically zero. The reason is that the two idempotent components are independent, and one can vanish while the other does not.

## Singularities

### Classification

Let $f$ be split complex differentiable on a punctured disk $0 < \|z - z_0\|_E < R$.

**Removable singularity.** $z_0$ is removable if $f$ extends to a split complex differentiable function on $\|z - z_0\|_E < R$.

**Pole.** $z_0$ is a pole if $f(z) \to \infty$ in Euclidean modulus as $z \to z_0$.

**Essential singularity.** $z_0$ is an essential singularity if it is neither removable nor a pole.

**Caution.** The classification is more complicated than in the complex case, because the function can behave differently on the two idempotent components. A point can be removable for one component and a pole for the other, in which case it is neither removable nor a pole for the split complex function.

### Residues

There is **no** general residue theory in split complex analysis. The reason is that the integral around a singularity depends on the path, and there is no single number that captures the singularity.

In the idempotent basis, each component has its own residue, and the two residues are independent. The sum of the two residues is the analogue of the complex residue, but it does not determine the integral in general.

## Applications

### The Wave Equation

The split Cauchy–Riemann equations imply that the real and imaginary parts of a split complex differentiable function satisfy the wave equation

$$
\frac{\partial^2 u}{\partial x^2} - \frac{\partial^2 u}{\partial y^2} = 0.
$$

So split complex analysis is the natural setting for the study of the two-dimensional wave equation. The idempotent decomposition corresponds to the decomposition of a solution into left-moving and right-moving waves:

$$
u(x, y) = F(x + y) + G(x - y),
$$

where $F$ and $G$ are arbitrary differentiable functions. This is d'Alembert's solution, and it is the general solution of the wave equation in one spatial dimension.

### Hyperbolic Geometry

The split complex numbers are the natural coordinates for the hyperbolic plane. The **hyperbolic metric** is

$$
ds^2 = \frac{dx^2 - dy^2}{y^2},
$$

and the split complex differentiable functions that preserve this metric are the **hyperbolic isometries**, which are the analogues of the Möbius transformations in complex analysis.

### Signal Processing

The split complex Fourier transform, restricted to a bounded interval or with a decaying kernel, is used in the analysis of transient signals. The transform diagonalizes the wave operator, and the idempotent decomposition corresponds to the decomposition into forward and backward propagating waves.

## Comparison with Complex Analysis

The differences between split complex analysis and complex analysis are consequences of the sign in the multiplication rule $j^2 = +1$ versus $i^2 = -1$.

| Property | Complex | Split Complex |
|---|---|---|
| Multiplication | $i^2 = -1$ | $j^2 = +1$ |
| Zero divisors | none | $1 \pm j$ |
| Cauchy–Riemann | $u_x = v_y$, $u_y = -v_x$ | $u_x = v_y$, $u_y = v_x$ |
| Harmonic equation | $\Delta u = 0$ | $\Box u = 0$ |
| Cauchy integral | yes | no |
| Residue theory | yes | no |
| Liouville | yes | no |
| Identity theorem | yes | no |
| Conformality | yes | no |
| Idempotent decomposition | no | yes |

The complex case is rigid: differentiability is a strong condition, and it forces the function to be determined by its boundary values. The split complex case is flexible: differentiability is a weak condition, and the function is determined by two independent real functions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $j$ | Split imaginary unit, $j^2 = +1$ |
| $z = x + jy$ | General split complex number |
| $\bar{z} = x - jy$ | Split complex conjugate |
| $\|z\|_E = \sqrt{x^2 + y^2}$ | Euclidean modulus |
| $\|z\| = \sqrt{\|x^2 - y^2\|}$ | Split modulus |
| $B(z_0, r)$ | Open disk of radius $r$ |
| $f'(z)$ | Split complex derivative |
| $\partial/\partial z, \partial/\partial \bar{z}$ | Split Wirtinger derivatives |
| $e_+ = (1 + j)/2$ | Positive idempotent |
| $e_- = (1 - j)/2$ | Negative idempotent |
| $z = z_+ e_+ + z_- e_-$ | Idempotent decomposition |
| $\int_\gamma f(z) \, dz$ | Contour integral |
| $\Box = \partial_x^2 - \partial_y^2$ | d'Alembertian |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of SL(2, ℝ)* (Imperial College Press, 2012), for the analytic applications.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.


