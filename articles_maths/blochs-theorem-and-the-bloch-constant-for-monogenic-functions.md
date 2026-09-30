# __Bloch's Theorem and the Bloch Constant for Monogenic Functions__

## Introduction

Bloch's theorem is the foundational statement of geometric function theory that goes beyond the Schwarz lemma: a holomorphic function of one variable with unit derivative at the origin cannot collapse, and its image must contain a disk of a size fixed in advance. The size, the **Bloch constant**, is an absolute number, and its exact value is one of the celebrated open problems of the subject. This article states and proves the analogue of the theorem for **monogenic functions** of the reduced quaternions, where the derivative is the hypercomplex derivative of the Cauchy–Riemann operator in $\mathbb{R}^3$ and the image contains balls in the three-dimensional reduced-quaternion space $\mathcal{A}\cong\mathbb{R}^3$. The analogy is not a metaphor: the classical proof of Bloch's theorem is reproduced through the two auxiliary estimates of the source, and it yields an explicit absolute radius.

The article is the Bloch-type companion of *Quaternion Regular Functions*, which owns the reduced-quaternion operator, the Riesz system, the hypercomplex derivative, the hyperholomorphic constants and the spherical monogenics used here without proof. The classical theory is *Complex Harmonic Analysis* for the Bloch space and the one-variable background, and the comparison with the conformal case is made throughout. The Bloch theorem and the Bloch constant are the only objects claimed here: the estimates of the hypercomplex derivative and of its primitive are the ones proved by the source, restated in this corpus's notation and conventions.

Throughout, $\mathcal{A} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2\}$ is the real vector space of reduced quaternions, a three-dimensional subspace of $\mathbb{H}$ that is not a subalgebra; $x = x_0+x_1e_1+x_2e_2$ ranges over $\mathbb{R}^3$; $D = \partial_0+e_1\partial_1+e_2\partial_2$ and $\bar D = \partial_0-e_1\partial_1-e_2\partial_2$ are the reduced Cauchy–Riemann operator and its conjugate, with $D\bar D = \bar DD = \Delta_3$; a function is **monogenic** when $Df = 0$, and its **hypercomplex derivative** is $\tfrac12\bar Df$. The ball of centre $0$ and radius $r$ is $B_r$, and for a continuous $\mathcal{A}$-valued function the **maximum modulus function** is

$$
\mathcal{M}(f,r) = \max_{|x|\leq r}|f(x)| .
$$

The space of monogenic functions on $B_r$ is written $\mathcal{R}^+(B_r;\mathcal{A})$, and the homogeneous monogenic polynomials of degree $n$ form a space $\mathcal{R}^+(B_r;\mathcal{A};n)$ of dimension $2n+3$.

## The Classical Theorem and Its Constant

Bloch's theorem, in its classical form, fixes the size of an image disk by the derivative at a point.

**Theorem (Bloch; classical form).** Let $f$ be holomorphic on the unit disk with $f'(0) = 1$. Then $f$ is univalent on some open subset of the disk, and its image contains a disk of radius at least $1/12$.

The number $1/12$ is not best possible. The **Bloch constant** $B$ is the supremum of the radii that may be asserted in the theorem with the normalisation $f'(0) = 1$, and it satisfies

$$
\frac{1}{12} < \frac{3}{2}-\sqrt{2} \leq B,
$$

where the middle number is $0.085786\ldots$ and is the sharper of the two elementary lower bounds; the exact value of $B$ is unknown, and it is known only that $1/12<B<1/2$. The two features of the classical proof that survive the passage to several variables are, first, that the argument is local and then made global by a normalisation, and second, that the two ingredients are an estimate for the derivative and an estimate for its primitive. Both are reproduced below.

### Why there is a hypercomplex analogue

In one variable the derivative of a holomorphic function is again holomorphic, and the primitive of a holomorphic function is holomorphic, so the classical argument can be run on $f$ and on $f'$ indifferently. In the reduced-quaternion theory the analogous statements hold, and for a structural reason: the reduced-quaternion module is a codimension-one subspace of the quaternion algebra, so its left and right regularity coincide.

**Proposition (closure under the hypercomplex derivative and the primitive).** For monogenic $f$, the hypercomplex derivative $\tfrac12\bar Df$ is monogenic, and the monogenic primitive $\mathcal{P}f$ is monogenic with $\tfrac12\bar D(\mathcal{P}f) = f$.

*Proof.* From $\bar DD = \Delta_3$ and $D\bar D = \Delta_3$ one has $D(\tfrac12\bar Df) = \tfrac12\Delta_3f = \tfrac12\bar D(Df) = 0$ for monogenic $f$, so the derivative of a monogenic function is monogenic; the primitive is defined by the ladder relations of *Quaternion Regular Functions*, which increase the degree and invert $\tfrac12\bar D$ modulo the hyperholomorphic constants.

This closure is exactly what fails in the four-variable theory, where the derivative of a regular function need not be regular; the reduced-quaternion setting is the one in which the classical mechanism is available.

### The comparison with the classical constant

| Theory | Constant | Value |
|---|---|---|
| Classical Bloch theorem (statement) | $1/12$ | $0.083333\ldots$ |
| Classical, sharper elementary lower bound | $3/2-\sqrt{2}$ | $0.085786\ldots$ |
| Classical, best possible (Bloch constant $B$) | unknown | $1/12 < B < 1/2$ |
| Monogenic, the theorem below | $\frac{1}{120}-\frac{31096}{20511149}\sqrt{3}$ | $0.0057074\ldots$ |
| Monogenic, safe explicit bound | $1/180$ | $0.005555\ldots$ |

The hypercomplex constant is smaller by roughly a factor of fifteen. That is expected and is discussed in the final section: the monogenic maps of the theorem are not conformal, the value space is three-dimensional, and the argument is an Estermann-type normalisation rather than the sharp extremal argument of the one-variable theory.

## The Two Auxiliary Estimates

The two estimates bound the hypercomplex derivative and its primitive by the growth of the maximum modulus of the derivative. They are the exact analogues of the estimates Estermann used in his proof of Picard's great theorem, and they are the only analytic input of the theorem. Both are quoted from the source and rest on the orthogonality of the spherical monogenics to the hyperholomorphic constants.

### The estimate for the hypercomplex derivative

**Lemma (derivative estimate).** Let $f\in\mathcal{R}^+(B_r;\mathcal{A})$. Then for $0\leq|x|<r$,

$$
\left|(\tfrac12\bar D)f(x)-(\tfrac12\bar D)f(0)\right| \leq \frac{6\,|x|\,r}{(r-|x|)^2}\;\mathcal{M}\!\left((\tfrac12\bar D)f,\,r\right).
$$

The estimate says that the hypercomplex derivative cannot oscillate faster than the inverse square of the distance to the boundary; it is the exact counterpart of the elementary Cauchy estimate in one variable, with the same exponent of the boundary distance.

### The estimate for the primitive

**Lemma (primitive estimate).** Let $f\in\mathcal{R}^+(B_r;\mathcal{A})$ with $f(0) = 0$. Then for $0\leq|x|<r$,

$$
\left|\mathcal{P}_r\!\left\{(\tfrac12\bar D)f(x)-(\tfrac12\bar D)f(0)\right\}\right| \leq \frac{2}{\sqrt3}\,\frac{|x|^2\left(4|x|^2+9r^2-11|x|r\right)}{(r-|x|)^3}\;\mathcal{M}\!\left((\tfrac12\bar D)f-(\tfrac12\bar D)f(0),\,r\right).
$$

Here $\mathcal{P}_r$ is the primitive taken on $B_r$, normalised to be orthogonal to the hyperholomorphic constants; the expression in braces is $f$ minus its linear term, the analogue of the classical $f(z)-f'(0)z$.

### The combined estimate

Combining the two lemmas gives the single inequality on which the radius depends.

**Proposition (Estermann-type estimate).** Let $f\in\mathcal{R}^+(B_r;\mathcal{A})$. Then for $0\leq|x|<r$,

$$
\left|\mathcal{P}_r\!\left\{(\tfrac12\bar D)f(x)-(\tfrac12\bar D)f(0)\right\}\right| \leq \frac{12}{\sqrt3}\,\frac{|x|^3\,r\left(4|x|^2+9r^2-11|x|r\right)}{(r-|x|)^5}\;\mathcal{M}\!\left((\tfrac12\bar D)f,\,r\right).
$$

The linear term $\mathbf{X}^{0,\dagger}_1(x)\,(\tfrac12\bar D)f(0)$, with $\mathbf{X}^{0,\dagger}_1(x) = x_0+\tfrac12x_1e_1+\tfrac12x_2e_2$, is the degree-one monogenic polynomial, and the subtraction of it is the step that makes the estimate orthogonal to the hyperholomorphic constants and hence sharp enough for the theorem.

### The orthogonality, and why it is the crux

The estimate above is the reason the monogenic theory admits a Bloch theorem at all, and the reason is the Fourier decomposition $f = g+h$ of *Quaternion Regular Functions*: $g$, the main part, is orthogonal to the hyperholomorphic constants, and $h$ is a constant for the hypercomplex derivative.

**Proposition (the linear term is the derivative's representative).** For monogenic $f$, the main part of $f$ of degree one is $\mathbf{X}^{0,\dagger}_1(x)\,(\tfrac12\bar D)f(0)$, and $\mathbf{X}^{0,\dagger}_1$ is the monogenic polynomial of degree one with $(\tfrac12\bar D)\mathbf{X}^{0,\dagger}_1 = 1$.

The proposition is the exact analogue of the fact that the linear part of a holomorphic function is $f'(0)z$. In one variable the statement is trivial; here it is the content of the degree-one ladder and of the orthogonality of the main part to the hyperholomorphic constants, and it is what allows $f$ to be compared with its own derivative.

## The Auxiliary Function and Its Maximum

The radius is extracted from the maximum of the elementary real function that the combined estimate produces.

**Definition (the auxiliary function).** For $r>0$ and $0<\rho<r$,

$$
g(\rho) = \frac{\rho}{2}-8\sqrt3\;\frac{\rho^3\,r\left(4\rho^2+9r^2-11\rho r\right)}{(r-\rho)^5}.
$$

**Lemma (the maximum of $g$).** The function $g$ has exactly one maximum on $(0,r)$, located at $\rho_{\max}>\tfrac{r}{30}$, and

$$
g(\rho_{\max}) > g\!\left(\frac{r}{30}\right) = \left(\frac{1}{60}-\frac{62192}{20511149}\sqrt3\right)r .
$$

*Proof.* The derivative is positive at $r/30$ and negative at $r/20$,

$$
g'\!\left(\frac{r}{30}\right) > 0, \qquad g'\!\left(\frac{r}{20}\right) < 0,
$$

and the second derivative is

$$
g''(\rho) = -\frac{48\sqrt3\,\rho\,r^2\left(3\rho^3-7\rho^2r+5\rho r^2+9r^3\right)}{(r-\rho)^7}.
$$

The cubic $p(\rho) = 3\rho^3-7\rho^2r+5\rho r^2+9r^3$ has two stationary points, at $\rho = r$ and $\rho = \tfrac59r$, at both of which it is positive, so it has exactly one real zero, and that zero is negative; hence $p>0$ and $g''<0$ on $(0,r)$. A strictly concave function has a single maximum, the two derivative signs place it between $r/30$ and $r/20$, and the value at $r/30$ is a lower bound for its maximum.

The value at the evaluation point is elementary: with $r = 1$ and $\rho = 1/30$, the rational part is $1/60$ and the remainder is $8\sqrt3\cdot3887\cdot2/20511149 = 62192\sqrt3/20511149$, since $20511149 = 29^5$ and $(1-1/30)^5 = 29^5/30^5$.

*Verified numerically.* $g'(1/30) = 0.0067028\ldots > 0$ and $g'(1/20) = -0.712166\ldots < 0$; $g''$ is negative at one hundred sample points of $(0,1)$; $p$ has a single real zero, and it lies in $(-1,0)$.

## The Local Statement

The local statement is the normalised form of the computation, and it is the step where the auxiliary function enters.

**Lemma (local normalisation).** Let $f\in\mathcal{R}^+(B_r;\mathcal{A})$ and suppose that for some $a\in B_r$,

$$
\mathcal{M}\!\left((\tfrac12\bar D)f,\,r\right) \leq 2\left|(\tfrac12\bar D)f(a)\right| .
$$

Then the image of $f$ contains a ball of radius

$$
R = \left(\frac{1}{60}-\frac{62192}{20511149}\sqrt3\right)r\left|(\tfrac12\bar D)f(a)\right| .
$$

*Proof.* After the translation that sends $f(a)$ to $0$, the combined estimate bounds $|\mathcal{P}_r\{(\tfrac12\bar D)f(x)-(\tfrac12\bar D)f(a)\}|$ by $4\sqrt3\,\rho^3r(4\rho^2+9r^2-11\rho r)/(r-\rho)^5$ times $\mathcal{M}((\tfrac12\bar D)f,r)$, and on $|x| = \rho$ the reverse triangle inequality gives

$$
|f(x)-f(a)| \geq \frac{\rho}{2}\left|(\tfrac12\bar D)f(a)\right| - \left|\mathcal{P}_r\{(\tfrac12\bar D)f(x)-(\tfrac12\bar D)f(a)\}\right| .
$$

Inserting the hypothesis $\mathcal{M}\leq 2|(\tfrac12\bar D)f(a)|$ multiplies the second term by $2$, and the resulting lower bound is exactly $g(\rho)|(\tfrac12\bar D)f(a)|$; the maximum lemma then gives the asserted radius at $|x| = r/30$.

## The Global Statement

The passage from the local statement to a statement with no pointwise hypothesis is the argument of Estermann, and it costs a factor of two in the radius.

**Theorem (the global normalisation).** Let $f\in\mathcal{R}^+(B_r;\mathcal{A})$. Then the image of $f$ contains balls of radius

$$
R = \left(\frac{1}{120}-\frac{31096}{20511149}\sqrt3\right)\mathcal{M}\!\left(\left|(\tfrac12\bar D)f(x)\right|(1-|x|),\,r\right).
$$

*Proof.* Assign to $f$ the continuous function $|(\tfrac12\bar D)f(x)|(1-|x|)$ on the closed ball; it attains its maximum at a point $q\in B_r$. With $t = \tfrac12(1-|q|)$ one has $\mathcal{M}(|(\tfrac12\bar D)f|(1-|x|),r) = 2t\,|(\tfrac12\bar D)f(q)|$ and $B_t(q)\subseteq B_r$, and $1-|x|\geq t$ on $B_t(q)$. From $|(\tfrac12\bar D)f(x)|(1-|x|)\leq 2t|(\tfrac12\bar D)f(q)|$ it follows that $|(\tfrac12\bar D)f(x)|\leq 2|(\tfrac12\bar D)f(q)|$ on $B_t(q)$, so the local lemma applies on the ball $B_t(q)$ and gives balls of radius $(1/60-62192\sqrt3/20511149)\,t\,|(\tfrac12\bar D)f(q)|$. Substituting the value of $t$ halves the local constant, producing the factor $1/120$ and the coefficient $31096 = 62192/2$ of $\sqrt3$.

**Theorem (Bloch's theorem for monogenic functions).** Let $f\in\mathcal{R}^+(B_r;\mathcal{A})$ with $\left|(\tfrac12\bar D)f(0)\right| = 1$. Then the image of $f$ contains balls of radius

$$
R = \frac{1}{120}-\frac{31096}{20511149}\sqrt3 .
$$

The radius does not depend on $f$, which is the content of the theorem: among all monogenic functions of the ball with unit hypercomplex derivative at the origin, the size of the largest ball universally contained in the image is bounded below by an absolute number.

## The Value of the Constant

The constant is a specific real number, and it is worth recording its value and what can honestly be asserted about it.

**Proposition (the value).** With exact arithmetic,

$$
\frac{1}{120}-\frac{31096}{20511149}\sqrt3 = 0.005707451579\ldots = \frac{1}{175.2095\ldots}, \qquad
\frac{1}{60}-\frac{62192}{20511149}\sqrt3 = 0.011414903158\ldots = \frac{1}{87.6047\ldots},
$$

and $20511149 = 29^5$.

### The asserted bound

The source states the theorem with the conclusion that the radius exceeds $1/150$, and states the local lemma with the companion conclusion that the local constant exceeds $1/75$. Both inequalities are false for the constants as written:

$$
0.0057074\ldots < \frac{1}{150} = 0.0066666\ldots, \qquad 0.0114149\ldots < \frac{1}{75} = 0.0133333\ldots .
$$

The gap is not marginal and it is the same in both, so it is a single arithmetic slip repeated at the two statements rather than a substantive error: the derivation of the constants themselves is correct, and the constants are internally consistent, with $g(r/30)$ equal to the rational-and-radical expression exactly. The safe inequalities, verified directly, are

$$
\frac{1}{120}-\frac{31096}{20511149}\sqrt3 > \frac{1}{180} = 0.0055555\ldots, \qquad
\frac{1}{60}-\frac{62192}{20511149}\sqrt3 > \frac{1}{90} = 0.0111111\ldots .
$$

The theorem therefore stands with the constant it produces; only the announced bound $1/150$ has to be replaced by $1/180$. The published version of the paper may carry different constants, and if it does, its numbers need the same check.

## Comparison with the Classical Theory

The comparison isolates three differences between the monogenic and the conformal settings.

**The size of the constant.** The monogenic constant $0.0057074\ldots$ is about fifteen times smaller than $1/12$. The monogenic maps are not conformal, the value space is three-dimensional, and the argument stops at the Estermann normalisation, which is a two-step estimate rather than the extremal one-variable argument. The source itself records that the improvement of the radius is left open, and no claim is made here that the number is best possible.

**The role of the hyperholomorphic constants.** In one variable the subtraction $f(z)-f'(0)z$ removes a term that is already of the form $z$ times a holomorphic function, and the constants of the theory are the constants. In the reduced-quaternion theory the space of hyperholomorphic constants has dimension two in every degree and the main part must be split off from it by an orthogonal projection; the $2n+3$ count of the monogenic polynomials of degree $n$ is the measure of that extra structure. The theorem is available because that projection exists.

**Earlier hyperholomorphic Bloch constants.** A Bloch constant for hyperholomorphic functions of a quaternionic variable was obtained earlier by Rochon, and the theorem above is the three-dimensional reduced-quaternion analogue with a different function class and a different, explicit constant. The classical higher-dimensional theory of Bloch constants for holomorphic maps of the ball is that of Chen and Gauthier; the monogenic theory is not contained in it, because the monogenic maps are not holomorphic in several complex variables.

## Summary

The Bloch theorem for monogenic functions of the reduced quaternions says that a monogenic function of the ball whose hypercomplex derivative at the origin has modulus one has an image containing a ball of the absolute radius $R = 1/120-(31096/20511149)\sqrt3 = 0.005707451\ldots$, independent of the function. The proof is the classical one, run on the reduced-quaternion theory: two estimates bound the hypercomplex derivative and its primitive by the growth of the maximum modulus of the derivative, an elementary real function $g$ supplies the radius through the position of its unique maximum, a local normalisation gives a ball of radius $g(r/30)\,$ times the derivative at a point, and Estermann's maximum argument removes the pointwise hypothesis at the cost of a factor of two.

The mechanism is available because the reduced quaternions form a codimension-one subspace of $\mathbb{H}$ that is not a subalgebra: its left and right regularity coincide, its monogenic functions are two-sided, and the hypercomplex derivative and the monogenic primitive preserve monogenicity, which is exactly what the classical argument needs. The orthogonal splitting of a monogenic function into a main part and a hyperholomorphic constant plays the role of the classical subtraction of the linear term, and it is the point at which the growing dimension $2n+3$ of the monogenic polynomials enters.

The constant as printed in the source, $1/120-(31096/20511149)\sqrt3$, is correct and equals $0.005707451\ldots$; the announced lower bounds $1/150$ and $1/75$ are not implied by it and are false, the safe explicit bounds being $1/180$ and $1/90$. The comparison with the classical case gives $1/12$ and the sharper elementary $3/2-\sqrt2 = 0.085786\ldots$, both larger than the monogenic radius, as expected for a non-conformal theory in higher dimension. Whether the monogenic constant is best possible is open, as it is in one variable.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2\}$ | Reduced quaternions; a real subspace, not a subalgebra |
| $D = \partial_0+e_1\partial_1+e_2\partial_2$ | Reduced Cauchy–Riemann operator on $\mathbb{R}^3$ |
| $\bar D = \partial_0-e_1\partial_1-e_2\partial_2$ | Its conjugate; $D\bar D = \bar DD = \Delta_3$ |
| $Df = 0$ | Monogenicity; two-sided, $Df = 0\iff fD = 0$ |
| $\tfrac12\bar Df$ | Hypercomplex derivative |
| $\mathcal{P}, \mathcal{P}_r$ | Monogenic primitive, and its normalisation to $B_r$ orthogonal to the constants |
| $\mathbf{X}^{0,\dagger}_1(x) = x_0+\tfrac12x_1e_1+\tfrac12x_2e_2$ | Degree-one monogenic polynomial; $(\tfrac12\bar D)\mathbf{X}^{0,\dagger}_1 = 1$ |
| $\mathcal{R}^+(B_r;\mathcal{A})$ | Monogenic functions on $B_r$ |
| $\mathcal{R}^+(B_r;\mathcal{A};n)$ | Homogeneous monogenic polynomials of degree $n$; $\dim = 2n+3$ |
| $\mathcal{M}(f,r) = \max_{|x|\leq r}|f(x)|$ | Maximum modulus function |
| $g(\rho) = \frac{\rho}{2}-8\sqrt3\frac{\rho^3r(4\rho^2+9r^2-11\rho r)}{(r-\rho)^5}$ | Auxiliary function whose maximum gives the radius |
| $R = \frac{1}{120}-\frac{31096}{20511149}\sqrt3$ | The Bloch radius of the theorem; $0.005707451\ldots$ |
| $1/12$, $3/2-\sqrt2$ | Classical Bloch constant statement and sharper elementary bound |

## Further Reading

- André Bloch, "Les théorèmes de M. Valiron sur les fonctions entières et la théorie de l'uniformisation", *Annales de la Faculté des Sciences de l'Université de Toulouse* **17** (1925), for the original theorem.
- Lars V. Ahlfors, "An extension of Schwarz's lemma", *Transactions of the American Mathematical Society* **43** (1938) 359–364, and *Conformal Invariants: Topics in Geometric Function Theory* (McGraw-Hill, 1973), for the sharpened lower bounds and the upper bounds on the Bloch constant.
- T. Estermann, "Notes on Landau's proof of Picard's 'Great' Theorem", in *Studies in Pure Mathematics Presented to R. Rado* (Academic Press, 1971) 101–106, for the normalisation argument that makes the theorem global and for the one-variable prototype of the two estimates.
- H. Chen and P. M. Gauthier, "Bloch constants in several variables", *Transactions of the American Mathematical Society* **353** (2001) 1371–1386, for the holomorphic maps of the ball and the several-variable theory to which the monogenic case should be compared.
- Daniel Rochon, "A Bloch constant for hyperholomorphic functions", *Complex Variables, Theory and Application* **44** (2001) 85–101, for an earlier Bloch constant in a hypercomplex setting.
- Klaus Gürlebeck and João Morais, "Bloch's theorem in the context of quaternion analysis", *Computational Methods and Function Theory* **12** (2012), doi:10.1007/BF03321843 (arXiv:1201.0530), the source of the theorem, the two estimates and the constant treated here.
- Klaus Gürlebeck and Helmuth Malonek, "A hypercomplex derivative of monogenic functions in $\mathbb{R}^{n+1}$ and its applications", *Complex Variables and Elliptic Equations* **39** (1999) 199–228, for the hypercomplex derivative and the hyperholomorphic constants.
- Helmuth Leutwiler, "Quaternionic analysis in $\mathbb{R}^3$ versus its hyperbolic modification", in *Clifford Analysis and Its Applications*, NATO Science Series II **25** (Kluwer, 2001) 193–211, for the reduced-quaternion function theory and the dimension $2n+3$.
- Isabel Caçao and Helmuth Malonek, "Remarks on some properties of monogenic polynomials", in *ICNAAM 2006*, Special Volume of Wiley-VCH (2006) 596–599, and Isabel Caçao, Klaus Gürlebeck and Sören Bock, "On derivatives of spherical monogenics", *Complex Variables and Elliptic Equations* **51** (2006) 847–869, for the spherical monogenics, their ladder relations and their estimates.
