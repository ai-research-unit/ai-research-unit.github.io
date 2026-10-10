# __The Pluripotential Theory of the Biquaternion Dynamics__

## Introduction

The pluripotential theory of a polynomial map of $\mathbb{C}^k$ builds an equilibrium measure from the Green's function, and the measure is the bridge between the dynamics and the geometry: it is the harmonic measure of the fractal, the maximal-entropy measure, the limit of the distribution of the preimages of a point, and the source of the ergodic and the dimension statements of the modern theory. The biquaternion passage enlarges the dimension to $k=4$ and makes the map holomorphic, so the framework is available; the same passage breaks the properness of the leading part, so the theory is available only off the zero-divisor cone and its conclusions must be stated conditionally. This article assembles the framework, states the invariance of the equilibrium measure and its product form on the split subalgebra, and records precisely what the non-properness costs.

The Green's function and its conditional existence are *The Escape Radius and the Green's Function for the Biquaternions*; the quadratic family and its critical set are *The Biquaternion Quadratic Map and Its Julia Sets*; the zero divisors are *The Zero Divisors and the Singular Julia Sets*; the matrix model and the two-variable reading are *The Matrix Element Representation and the Biquaternion Dynamics*; the idempotent plane and its product structure are *The Idempotent Decomposition and the Split Fractal*. The general theory is *Plurisubharmonic Functions*, *Several Complex Variables* and *Several Complex Variables*, and the measure-theoretic background is *Fractal Analysis* of Part III.

The article owns the Monge–Ampère current of the biquaternion map, the invariance of the equilibrium measure under the map, the product form on the idempotent plane, the mass-loss phenomenon at the cone, and the statement of the open questions.

**Standing convention.** $F=F_{\tilde C}$ is the quadratic family in the general plain bilinear product, $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ the matrix model, $F^*$ the pullback on functions and currents, $d$ the algebraic degree $2$, and $k=4$ the complex dimension of the model.

## The Classical Framework

**Theorem (the equilibrium measure of a polynomial map).** Let $P:\mathbb{C}^k\to\mathbb{C}^k$ be a polynomial map of algebraic degree $d$ whose leading homogeneous part is proper, and let $G_P=\lim_{n\to\infty}d^{-n}\log^+\|P^n\|$ be its Green's function. Then $G_P$ is plurisubharmonic on $\mathbb{C}^k$ or identically $-\infty$, $P^*G_P=d\,G_P$, and

$$
\mu_P=(dd^cG_P)^k
$$

is a probability measure with $P^*\mu_P=d^k\mu_P$, supported on the Julia set of $P$, of maximal entropy $k\log d$, satisfying the equidistribution of preimages.

**Proof.** This is the theorem of Fornæss–Sibony and Bedford–Jonsson, presented in *Several Complex Variables* and *Plurisubharmonic Functions*; the invariance of the measure is the chain rule $P^*dd^cG=dd^c(P^*G)=d\,dd^cG$ raised to the power $k$, and the normalisation to a probability is the definition of $\mu_P$.

**Remark (what the properness of the leading part buys).** The properness of the leading homogeneous part is what makes the pullback of $dd^cG$ a current of the right mass, equivalently what makes the map regular in the sense that the pullback of the class of the hyperplane has the expected degree. **The biquaternion map fails exactly this hypothesis, and the failure is measurable: the leading part $\tilde Q\mapsto\tilde Q^2$ has the square-zero cone as its fibre over $0$, so some of the pullback mass is lost on the cone.**

## The Green's Function and the Current

**Proposition (the current and its invariance).** Let $\tilde C=Ce_0$ be central and let $G_{\tilde C}$ be the Green's function, defined on the regular part of the escaping set. On the open set where $G_{\tilde C}$ is plurisubharmonic and smooth, the current

$$
\gamma_{\tilde C}=(dd^cG_{\tilde C})^4
$$

is positive and satisfies $F^*\gamma_{\tilde C}=16\,\gamma_{\tilde C}$.

**Proof.** $F^*G_{\tilde C}=2G_{\tilde C}$ (*The Escape Radius and the Green's Function for the Biquaternions*), the pullback commutes with $dd^c$, and $dd^c(2G)=2\,dd^cG$; raising to the fourth power multiplies the current by $2^4=16$.

**Remark (the degree and the exponent).** The base of the invariance is the algebraic degree $2$ and the exponent is the complex dimension $4$, so the multiplier is $16$ and the entropy of the measure is $4\log2$. **The biquaternion map has a four-dimensional equilibrium measure with the entropy of four complex degrees of freedom, one for each eigenvalue of the model.** On the central slice the entropy reduces to the two $(\log2)$-contributions of the two eigenvalues and the measure is the product of two one-variable equilibrium measures.

**Theorem (the product form on the idempotent plane).** Let $\tilde\Pi$ be a primitive idempotent and let $\tilde C=C_1\tilde\Pi+C_2\tilde\Pi'$ be in the idempotent plane. Then the equilibrium measure of the restriction is the product

$$
\mu_{\tilde C}\big|_{W_{\tilde\Pi}}=\mu_{C_1}\otimes\mu_{C_2},
$$

the product of the two one-variable equilibrium measures of $\zeta\mapsto\zeta^2+C_j$, and its entropy is $2\log2$.

**Proof.** On the plane the map is the pair of complex quadratic maps (*The Idempotent Decomposition and the Split Fractal*), the Green's function is the maximum of the two complex Green's functions (*The Escape Radius and the Green's Function for the Biquaternions*), and the Monge–Ampère current of a function of two independent complex variables is the product of the one-variable currents.

## The Mass Loss at the Cone

**Proposition (the pullback loses mass on the cone).** The equation $\tilde Q^2=\tilde W$ has four solutions for a generic regular value $\tilde W$ (*Biquaternion Square Roots of a General Element*), so the generic fibre of the square map has four points; at $\tilde W=0$ the equation is $\tilde Q^2=0$ and its solution set is the square-zero cone, of complex dimension two. The topological degree of the square map is therefore not locally constant at $0$: the fibre over $0$ has complex dimension two while the generic fibre has dimension zero.

**Proof.** The generic count is the corollary on the number of roots of *Biquaternion Square Roots of a General Element*: four roots when $(\boldsymbol{Q},\boldsymbol{Q})\neq0$ and $n\neq0$, since the reduced quadratic then has two distinct non-zero solutions and each contributes two scalar parts; the fibre over $0$ is the set of nilpotent elements, the cone $\{Q_0=0,\ (\mathbf Q,\mathbf Q)=0\}$ of complex dimension two. The derivative of the square map at $\tilde Q$ is $\tilde P\mapsto\tilde Q\tilde P+\tilde P\tilde Q$, singular exactly on the critical set; at a square-zero point it is nilpotent with image of complex dimension two, so the map is not locally finite there.

**Remark (the consequence for the measure).** A polynomial map whose leading part is proper pulls back a generic point to exactly $d^k$ preimages, counted with multiplicity, so the preimage measure equidistributes; the biquaternion map pulls back $0$ to a positive-dimensional cone, and the preimages of a point outside the cone may have limit points in the cone. **The equidistribution of preimages holds away from the cone and gains a correction term from the cone; the correction is not known in closed form, and this is the technical core of the open problem of the category.**

## The Exceptional Set and the Small Fractal

**Definition.** The **exceptional set** of the biquaternion map is the set of the points $\tilde Q$ whose orbit fails to have the generic local behaviour: the critical set $\Sigma(\mathbb{B})=\mathscr{Z}\cup\mathrm{Vect}(\mathbb{B})$, together with the set where the Green's function fails to be plurisubharmonic.

**Remark (the small Julia set).** In the several-variable theory the support of the equilibrium measure is the *small Julia set*, contained in the Julia set and possibly strictly smaller, and it is the closure of the union of the backward images of the critical set. For the biquaternion map the critical set is the union of the cone and the vector subspace, so the small Julia set is the closure of the union of the backward images of that union; whether it equals the Julia set is a question with no answer at present, because the equidistribution it rests on is the one obstructed by the cone. **The article states the small Julia set as the support of the measure and does not identify it with the Julia set.**

**Remark (the ergodic properties expected).** The measure, where it exists, is expected to be mixing, of maximal entropy $4\log2$, and to satisfy the central limit theorem and the large-deviation principle of the one-variable theory; on the idempotent plane all of these hold because the theory factors, and off the plane each of them is conditional on the regularity that the cone obstructs.

## Summary

The pluripotential framework of a polynomial map of $\mathbb{C}^4$ applies to the biquaternion map wherever the Green's function is defined and plurisubharmonic, and there the current $(dd^cG)^4$ is positive and invariant with multiplier $16$, the square of the algebraic degree raised to the complex dimension, so the equilibrium measure has maximal entropy $4\log2$. On an idempotent plane the theory factors exactly: the Green's function is the maximum of the two complex ones and the equilibrium measure is the product of the two one-variable equilibrium measures with entropy $2\log2$. The leading part of the map is not proper, its fibre over $0$ is the real four-dimensional square-zero cone, the topological degree is not locally constant there, and the pullback loses mass on the cone; the equidistribution of preimages and with it the identification of the small Julia set with the Julia set are therefore open, and the article states them as such. The exceptional set is the critical set of the map, the union of the cone and the vector subspace.

## Summary of Notation

| symbol | meaning |
|---|---|
| $G_{\tilde C}$ | the Green's function of the biquaternion map |
| $d$ | the algebraic degree, $2$ |
| $k$ | the complex dimension of the model, $4$ |
| $dd^c$ | the Monge–Ampère operator |
| $\gamma_{\tilde C}=(dd^cG_{\tilde C})^4$ | the Monge–Ampère current |
| $\mu_{\tilde C}$ | the equilibrium measure |
| $\mu_{C}$ | the one-variable equilibrium measure of $\zeta\mapsto\zeta^2+C$ |
| $\Sigma(\mathbb{B})=\mathscr{Z}\cup\mathrm{Vect}(\mathbb{B})$ | the critical set |

## Further Reading

- *The Escape Radius and the Green's Function for the Biquaternions* (`articles_maths/the-escape-radius-and-the-greens-function-for-the-biquaternions.md`), for the Green's function and the conditional existence used here.
- *The Idempotent Decomposition and the Split Fractal* (`articles_maths/the-idempotent-decomposition-and-the-split-fractal.md`), for the factoring of the dynamics on the idempotent plane.
- *The Zero Divisors and the Singular Julia Sets* (`articles_maths/the-zero-divisors-and-the-singular-julia-sets.md`), for the cone that is the exceptional set of the map.
- *Several Complex Variables* (`articles_maths/several-complex-variables.md`), for the plurisubharmonic tools and the several-variable dynamics the article adapts.
- *The Self-Similar Measure and the Invariant Measure* (`articles_maths/the-self-similar-measure-and-the-invariant-measure.md`) and *Multifractal Analysis and the Legendre Transform* (`articles_maths/multifractal-analysis-and-the-legendre-transform.md`), for the measure-theoretic statements of the category.
