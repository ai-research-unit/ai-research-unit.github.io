
# __Split Complex Analysis__

## Introduction

This article introduces split complex analysis as the study of differentiable functions of a split complex variable. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The split complex algebra is assumed from the article on split complex algebra, and the idempotent decomposition is used throughout. No physics is invoked. The hyperbolic structure that replaces the circular structure of complex analysis is developed systematically.

## The Split Complex Plane

### Points and Distance

A split complex number is written

$$
A = a + j a', \qquad a, a' \in \mathbb{R},
$$

where $j^2 = +1$. The real number $a$ is the **real part**, and $a'$ is the **imaginary part**. We write $a = \operatorname{Re} A$ and $a' = \operatorname{Im} A$.

The **Euclidean modulus** of $A$ is

$$
\|A\|_E = \sqrt{a^2 + a'^2},
$$

and the **Euclidean distance** between two split complex numbers $A$ and $B$ is

$$
d(A, B) = \|A - B\|_E.
$$

This makes $\mathbb{D}$ a metric space isometric to $\mathbb{R}^2$. The Euclidean modulus satisfies the triangle inequality and is positive-definite, so it is a genuine norm.

The **split modulus** is

$$
\rho = \sqrt{|a^2 - a'^2|},
$$

which is not a norm. It vanishes on the null cone $a = \pm a'$, and it is not subadditive; the quadratic form $a^2-a'^2$ from which it is built is indefinite. It is used in the study of the multiplicative structure, not the topological structure.

### Balls and Neighborhoods

The **open ball** of radius $r > 0$ centered at $A_0$ is

$$
B(A_0, r) = \{A \in \mathbb{D} : \|A - A_0\|_E < r\}.
$$

It is an open disk in the split complex plane, exactly as in the complex plane. The topology of $\mathbb{D}$ is the ordinary Euclidean topology of $\mathbb{R}^2$.

### Open and Closed Sets

A set $U \subseteq \mathbb{D}$ is **open** if for every $A_0 \in U$ there exists $r > 0$ with $B(A_0, r) \subseteq U$.

A set $F \subseteq \mathbb{D}$ is **closed** if its complement $\mathbb{D} \setminus F$ is open.

Arbitrary unions of open sets are open. Finite intersections of open sets are open. Dually for closed sets.

### Connectedness and Domains

A set $U \subseteq \mathbb{D}$ is **connected** if it cannot be written as the disjoint union of two non-empty sets open in $U$. It is **path-connected** if any two points can be joined by a continuous path in $U$. For open subsets of $\mathbb{D}$, connectedness and path-connectedness are equivalent.

A **domain** is a non-empty open connected subset of $\mathbb{D}$. Domains are the natural setting for split complex analysis, because differentiability on a domain imposes constraints that are weaker than in the complex case but still nontrivial.

### Compactness

A set $K \subseteq \mathbb{D}$ is **compact** if every open cover of $K$ has a finite subcover.

**Theorem (Heine–Borel).** A subset of $\mathbb{D}$ is compact iff it is closed and bounded in the Euclidean norm.

**Theorem.** A continuous split-complex-valued function on a compact set is bounded and attains its maximum and minimum Euclidean modulus.

## Limits and Continuity

### Limits of Sequences

A sequence $(A_n)$ of split complex numbers **converges** to $L \in \mathbb{D}$ if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
n \geq N \implies \|A_n - L\|_E < \epsilon.
$$

We write $A_n \to L$ or $\lim_{n \to \infty} A_n = L$.

**Uniqueness.** If $A_n \to L$ and $A_n \to L'$, then $L = L'$.

**Componentwise convergence.** Write $A_n = a_n + j a'_n$ and $L = a + j a'$. Then

$$
A_n \to L \iff a_n \to a \text{ and } a'_n \to a'.
$$

This is the reason split complex convergence is no harder than real convergence: it is two real convergences in parallel.

**Boundedness.** Every convergent sequence is bounded. The converse fails.

**Algebra of limits.** If $A_n \to L$ and $B_n \to M$, then

$$
A_n + B_n \to L + M, \qquad A_n B_n \to L M.
$$

There is no quotient rule in general, because $\mathbb{D}$ has zero divisors.

### Cauchy Sequences

A sequence $(A_n)$ is **Cauchy** if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
m, n \geq N \implies \|A_m - A_n\|_E < \epsilon.
$$

**Theorem.** In $\mathbb{D}$, a sequence converges iff it is Cauchy. This is the completeness of $\mathbb{D}$ as a metric space, and it follows from the completeness of $\mathbb{R}$ applied to the real and imaginary parts.

### Limits of Functions

Let $f : D \to \mathbb{D}$ with $D \subseteq \mathbb{D}$, and let $A_0$ be a limit point of $D$. We say

$$
\lim_{A \to A_0} f(A) = L
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
A \in D, \; 0 < \|A - A_0\|_E < \delta \implies \|f(A) - L\|_E < \epsilon.
$$

**Uniqueness.** If the limit exists, it is unique.

**Sequential criterion.** $\lim_{A \to A_0} f(A) = L$ iff for every sequence $(A_n)$ in $D \setminus \{A_0\}$ with $A_n \to A_0$, we have $f(A_n) \to L$.

**Algebra of limits.** Sums and products of limits are the limits of the sums and products.

### Continuity

A function $f : D \to \mathbb{D}$ is **continuous at** $A_0 \in D$ if

$$
\lim_{A \to A_0} f(A) = f(A_0).
$$

Equivalently, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
A \in D, \; \|A - A_0\|_E < \delta \implies \|f(A) - f(A_0)\|_E < \epsilon.
$$

$f$ is **continuous on** $D$ if it is continuous at every point of $D$.

**Theorem.** Sums and products of continuous functions are continuous. Compositions of continuous functions are continuous.

**Theorem.** $f$ is continuous iff the preimage of every open set is open. Equivalently, the preimage of every closed set is closed.

**Componentwise continuity.** Write $f(A) = u(a, a') + j v(a, a')$. Then $f$ is continuous at $A_0 = a_0 + j a'_0$ iff $u$ and $v$ are continuous at $(a_0, a'_0)$. This reduces split complex continuity to real continuity of two functions of two variables.

### Uniform Continuity

A function $f : D \to \mathbb{D}$ is **uniformly continuous** if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
A, B \in D, \; \|A - B\|_E < \delta \implies \|f(A) - f(B)\|_E < \epsilon.
$$

**Theorem.** A continuous function on a compact set is uniformly continuous.

## Split Complex Differentiability

### The Derivative

Let $f : U \to \mathbb{D}$ with $U$ open, and let $A_0 \in U$. The **derivative** of $f$ at $A_0$ is

$$
f'(A_0) = \lim_{h \to 0} \frac{f(A_0 + h) - f(A_0)}{h},
$$

provided the limit exists. If it does, $f$ is **split complex differentiable** at $A_0$, or **holomorphic** at $A_0$ in the split sense.

The limit is taken in the split complex plane, so $h$ can approach $0$ from any direction. But because $\mathbb{D}$ has zero divisors, the quotient is not always defined, and the limit must be taken along paths where $h$ is invertible. This is the fundamental difference from the complex case.

**Theorem.** Split complex differentiability implies continuity. The converse fails.

### The Cauchy–Riemann Equations

Write $f(A) = u(a, a') + j v(a, a')$, where $A = a + ja'$ and $u, v : U \to \mathbb{R}$.

**Theorem.** $f$ is split complex differentiable at $A_0 = a_0 + j a'_0$ iff $u$ and $v$ are real differentiable at $(a_0, a'_0)$ and satisfy the **split Cauchy–Riemann equations**

$$
\frac{\partial u}{\partial a} = \frac{\partial v}{\partial a'}, \qquad \frac{\partial u}{\partial a'} = \frac{\partial v}{\partial a}.
$$

**Proof.** Write $h = h_1 + j h_2$. The difference quotient is

$$
\frac{f(A_0 + h) - f(A_0)}{h} = \frac{(u_a h_1 + u_{a'} h_2) + j (v_a h_1 + v_{a'} h_2)}{h_1 + j h_2} + o(1).
$$

For the limit to exist independently of the direction of $h$, the numerator must be a split complex multiple of $h$. This forces the split Cauchy–Riemann equations.

**Corollary.** If $f$ is split complex differentiable, then $u$ and $v$ satisfy the **wave equation**:

$$
\frac{\partial^2 u}{\partial a^2} - \frac{\partial^2 u}{\partial a'^2} = 0, \qquad \frac{\partial^2 v}{\partial a^2} - \frac{\partial^2 v}{\partial a'^2} = 0.
$$

**Proof.** Differentiate the split Cauchy–Riemann equations and use the equality of mixed partials.

This is the fundamental difference from complex analysis: the real and imaginary parts of a holomorphic function are harmonic in the complex case, and solutions of the wave equation in the split complex case. The change of sign in the Cauchy–Riemann equations changes the Laplacian into the d'Alembertian.

### The Wirtinger Derivatives

Define the **split Wirtinger derivatives**

$$
\frac{\partial}{\partial A} = \frac{1}{2}\left( \frac{\partial}{\partial a} + j \frac{\partial}{\partial a'} \right), \qquad \frac{\partial}{\partial \bar{A}} = \frac{1}{2}\left( \frac{\partial}{\partial a} - j \frac{\partial}{\partial a'} \right).
$$

**Theorem.** $f$ is split complex differentiable iff $f$ is real differentiable and $\partial f / \partial \bar{A} = 0$. In that case,

$$
f'(A) = \frac{\partial f}{\partial A}.
$$

The condition $\partial f / \partial \bar{A} = 0$ is the split Cauchy–Riemann equations in compact form.

### Rules of Differentiation

**Linearity.** $(af + bg)' = a f' + b g'$.

**Product rule.** $(fg)' = f' g + f g'$.

**Quotient rule.** $(f/g)' = (f' g - f g')/g^2$ where $g$ is invertible.

**Chain rule.** $(f \circ g)'(A) = f'(g(A)) g'(A)$.

**Inverse function rule.** If $f$ is split complex differentiable at $A_0$ with $f'(A_0)$ invertible and $f^{-1}$ is defined near $f(A_0)$, then

$$
(f^{-1})'(f(A_0)) = \frac{1}{f'(A_0)}.
$$

## The Idempotent Decomposition

### Definition

The **idempotents** of $\mathbb{D}$ are

$$
\Pi_1 = \frac{1 + j}{2}, \qquad \Pi_2 = \frac{1 - j}{2}.
$$

They satisfy $\Pi_1^2 = \Pi_1$, $\Pi_2^2 = \Pi_2$, $\Pi_1 \Pi_2 = 0$, and $\Pi_1 + \Pi_2 = 1$.

Every split complex number decomposes uniquely as

$$
A = A_+ \Pi_1 + A_- \Pi_2, \qquad A_+ = a + a', \quad A_- = a - a'.
$$

### Differentiability in the Idempotent Basis

Write $f(A) = f_+(A) \Pi_1 + f_-(A) \Pi_2$, where $f_+$ and $f_-$ are real-valued functions. Then

$$
f \text{ is split complex differentiable} \iff f_+ \text{ is differentiable in } A_+ \text{ and } f_- \text{ is differentiable in } A_-.
$$

**Proof.** In the idempotent basis, the split complex algebra is $\mathbb{R} \oplus \mathbb{R}$, and the multiplication is componentwise. So a function $f$ is differentiable iff each component is differentiable with respect to its own variable.

This is the **fundamental theorem of split complex analysis**: differentiability in $\mathbb{D}$ is equivalent to differentiability in each of the two real components separately. There is no interaction between the two components, because the idempotents annihilate each other.

### Consequences

**No conformality.** Split complex differentiable functions do not preserve angles in general, because the two components can scale differently.

**No Cauchy integral formula.** There is no single integral formula that reconstructs a split complex differentiable function from its boundary values, because the two components are independent.

**No Liouville theorem.** A bounded split complex differentiable function on all of $\mathbb{D}$ need not be constant, because each component can be an arbitrary bounded differentiable function of one real variable.

## Integration

### Contour Integrals

Let $\gamma : [a, b] \to \mathbb{D}$ be a piecewise continuously differentiable path, and let $f$ be continuous on the image of $\gamma$. The **contour integral** of $f$ along $\gamma$ is

$$
\int_\gamma f(A) \, dA = \int_a^b f(\gamma(t)) \gamma'(t) \, dt.
$$

**Linearity.** $\int_\gamma (af + bg) = a \int_\gamma f + b \int_\gamma g$.

**Reversal.** $\int_{-\gamma} f = -\int_\gamma f$.

**Additivity.** If $\gamma$ is the concatenation of $\gamma_1$ and $\gamma_2$, then $\int_\gamma f = \int_{\gamma_1} f + \int_{\gamma_2} f$.

**Estimation.** If $\|f(A)\|_E \leq M$ on $\gamma$ and $L$ is the length of $\gamma$, then

$$
\left\| \int_\gamma f(A) \, dA \right\|_E \leq \sqrt{2} M L.
$$

The factor $\sqrt{2}$ is needed because the Euclidean modulus is not submultiplicative: $\|A B\|_E \leq \sqrt{2} \|A\|_E \|B\|_E$, and the constant is sharp.

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat, split version).** If $f$ is split complex differentiable on a simply connected domain $U$ and $\gamma$ is a closed contour in $U$, then

$$
\oint_\gamma f(A) \, dA = 0.
$$

**Proof.** In the idempotent basis, the integral decomposes into two real integrals, one for each component. Each component is a real line integral of a differentiable function of one variable, and each vanishes on a closed contour.

### The Cauchy Integral Formula

There is **no** general Cauchy integral formula in split complex analysis. The reason is that the kernel $1/(B - A)$ has a singularity on the null cone, and the integral around a point depends on the path in a way that cannot be removed by a single formula.

However, if the function is written in the idempotent basis, each component has its own Cauchy integral formula:

$$
f_+(A_+) = \frac{1}{2\pi i} \oint \frac{f_+(\zeta_+)}{\zeta_+ - A_+} \, d\zeta_+,
$$

and similarly for $f_-$. But these are complex formulas applied to real functions, and they require complexification of the components. They are not split complex formulas.

## Power Series

### Definition

A **power series** centered at $A_0$ is

$$
\sum_{n=0}^\infty c_n (A - A_0)^n, \qquad c_n \in \mathbb{D}.
$$

In the idempotent basis $c_n = c_{n,+} \Pi_1 + c_{n,-} \Pi_2$, and the series is the pair of real power series

$$
\sum_{n=0}^\infty c_{n,+} (A - A_0)_+^n \Pi_1 + \sum_{n=0}^\infty c_{n,-} (A - A_0)_-^n \Pi_2.
$$

The **radii of convergence** are the pair of real numbers

$$
R_\pm = \frac{1}{\limsup_{n \to \infty} |c_{n,\pm}|^{1/n}},
$$

with the conventions $R_\pm = 0$ if the limsup is $\infty$ and $R_\pm = \infty$ if the limsup is $0$.

**Theorem.** The series converges absolutely for $|A_+ - A_{0+}| < R_+$ and $|A_- - A_{0-}| < R_-$, and diverges if $|A_+ - A_{0+}| > R_+$ or $|A_- - A_{0-}| > R_-$. Where both inequalities hold it converges uniformly on compact subsets.

**Theorem.** A power series is split complex differentiable on the region $|A_+ - A_{0+}| < R_+$ and $|A_- - A_{0-}| < R_-$, and its derivative is obtained by term-by-term differentiation:

$$
\frac{d}{dA} \sum_{n=0}^\infty c_n (A - A_0)^n = \sum_{n=1}^\infty n c_n (A - A_0)^{n-1}.
$$

The differentiated series has the same radii of convergence.

### Taylor Series

**Theorem (Taylor, split version).** If $f$ is split complex differentiable on a domain containing the closed disk $\overline{B}(A_0, r)$, and its components $f_+$ and $f_-$ are real-analytic on that disk, then $f$ has a power series expansion

$$
f(A) = \sum_{n=0}^\infty \frac{f^{(n)}(A_0)}{n!} (A - A_0)^n
$$

valid for $\|A - A_0\|_E < r$.

**Proof.** In the idempotent basis, each component has a real Taylor expansion, and the two expansions combine.

**Corollary.** A split complex differentiable function whose components are real-analytic is analytic: it equals its Taylor series in a neighborhood of every point.

**Caution.** The identity theorem fails in general, because a split complex differentiable function can vanish on a set with an accumulation point without being identically zero. The reason is that the two idempotent components are independent, and one can vanish while the other does not.

## Singularities

### Classification

Let $f$ be split complex differentiable on a punctured disk $0 < \|A - A_0\|_E < R$.

**Removable singularity.** $A_0$ is removable if $f$ extends to a split complex differentiable function on $\|A - A_0\|_E < R$.

**Pole.** $A_0$ is a pole if $f(A) \to \infty$ in Euclidean modulus as $A \to A_0$.

**Essential singularity.** $A_0$ is an essential singularity if it is neither removable nor a pole.

**Caution.** The classification is empty under this hypothesis. The component $f_+$ is a function of $A_+$ alone, and differentiating $f$ at a point with $A_+ = A_{0+}$ and $A_- \neq A_{0-}$ (such points lie in the punctured disk) gives a derivative of $f_+$ across $A_{0+}$, and dually for $f_-$. So $f$ extends to $A_0$: every singularity in the sense above is removable, and there are no isolated poles or essential singularities. In particular a point that is a pole for one component is a pole for the function, since $\|f\|_E^2 = (f_+^2 + f_-^2)/2$.

### Residues

There is **no** general residue theory in split complex analysis. The reason is that the integral around a singularity depends on the path, and there is no single number that captures the singularity.

In the idempotent basis, each component has its own residue, and the two residues are independent. The sum of the two residues is the analogue of the complex residue, but it does not determine the integral in general.

## Comparison with Complex Analysis

The differences between split complex analysis and complex analysis are consequences of the sign in the multiplication rule $j^2 = +1$ versus $i^2 = -1$.

| Property | Complex | Split Complex |
|---|---|---|
| Multiplication | $i^2 = -1$ | $j^2 = +1$ |
| Zero divisors | none | $1 \pm j$ |
| Cauchy–Riemann | $u_a = v_{a'}$, $u_{a'} = -v_a$ | $u_a = v_{a'}$, $u_{a'} = v_a$ |
| Harmonic equation | $\Delta u = 0$ | $\Box u = 0$ |
| Cauchy integral | yes | no |
| Residue theory | yes | no |
| Liouville | yes | no |
| Identity theorem | yes | no |
| Conformality | yes | no |
| Idempotent decomposition | no | yes |

The complex case is rigid: differentiability is a strong condition, and it forces the function to be determined by its boundary values. The split complex case is flexible: differentiability is a weak condition, and the function is determined by two independent real functions.

## Summary

Split complex analysis is the study of differentiable functions of a split complex variable $A = a + ja'$ with $j^2 = +1$. The plane carries the Euclidean norm inherited from $\mathbb{R}^2$, and with it the convergent sequences and the continuous functions on which the subject is built.

The derivative is defined as in the complex case, and its behaviour is governed by the idempotents $\Pi_\pm = (1 \pm j)/2$, which satisfy $\Pi_1^2 = \Pi_1$, $\Pi_2^2 = \Pi_2$ and $\Pi_1\Pi_2 = 0$. In the idempotent basis the algebra is the direct sum $\mathbb{R} \oplus \mathbb{R}$, and the analysis decomposes with it: the power series and the conditions of differentiability separate into one condition for each component, so the theory is real analysis carried out twice rather than a new rigid theory as in the complex case.

The article develops the subject in that basis: contour integrals along paths, power series, and the classification of the isolated singularities as removable, a pole, or essential. It closes with the comparison with complex analysis and traces every difference to the sign in the multiplication rule, $j^2 = +1$ against $i^2 = -1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $j$ | Split imaginary unit, $j^2 = +1$ |
| $A = a + ja'$ | General split complex number |
| $\bar{A} = a - ja'$ | Split complex conjugate |
| $\|A\|_E = \sqrt{a^2 + a'^2}$ | Euclidean modulus |
| $\rho = \sqrt{|a^2 - a'^2|}$ | Split modulus |
| $B(A_0, r)$ | Open disk of radius $r$ |
| $f'(A)$ | Split complex derivative |
| $\partial/\partial A, \partial/\partial \bar{A}$ | Split Wirtinger derivatives |
| $\Pi_1 = (1 + j)/2$ | Positive idempotent |
| $\Pi_2 = (1 - j)/2$ | Negative idempotent |
| $A = A_+ \Pi_1 + A_- \Pi_2$ | Idempotent decomposition |
| $\int_\gamma f(A) \, dA$ | Contour integral |
| $\Box = \partial_a^2 - \partial_{a'}^2$ | d'Alembertian |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the comparison with the complex case.


