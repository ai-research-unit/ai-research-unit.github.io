
# Split-Quaternion Polar Representations

## Introduction

The article on split quaternion algebraic representations described four ways of writing a split quaternion using only the algebra operations, the split complex unit, and the underlying vector space structure: the split complex four-vector representation, the idempotent representation, the module representation, and the Clifford algebra representation.

This article describes the **polar representations** of the split quaternion algebra: ways of writing a split quaternion as a product of a modulus and an exponential. These representations use the exponential, and they are therefore not algebraic in the sense of the preceding article.

The word "representation" is used here in the sense of "a concrete realization of the algebra as a collection of computable objects." It is not used in the technical sense of algebra representation theory.

The polar representations of a split quaternion are **different in character** from the polar representations of a biquaternion, and it is important to be clear about why.

**The biquaternion case.** In the biquaternion algebra, the polar forms exist because the complex algebra contains the scalar imaginary $i$ with $i^2 = -1$, and because the biquaternion algebra contains a four-dimensional family of non-trivial roots of $-1$. The de Moivre formula

$$
e^{\rho\theta} = \cos\theta \, e_0 + \sin\theta \, \rho, \qquad \rho^2 = -e_0,
$$

holds for every root $\rho$ of $-1$, and this is what makes the exponential of a biquaternion computable in closed form. The two polar forms — the Hamilton form and the complex form — correspond to the two classes of roots of $-1$.

**The split quaternion case.** In the split quaternion algebra, the situation is different. The split complex algebra has the unit $j$ with $j^2 = +1$, **not** a square root of $-1$. The exponential of a split complex number is hyperbolic, not trigonometric:

$$
e^{j\theta} = \cosh\theta + j\sinh\theta.
$$

And the split quaternion algebra does contain roots of $-1$ — in fact, a four-dimensional family of them, as established in the article on split quaternion roots of minus one — but these roots are not central, and they do not generate a de Moivre formula for arbitrary exponentials. The exponential of a general split quaternion is not a product of a modulus and a phase in the same way as in the biquaternion case.

**The consequence.** The polar representations of a split quaternion are therefore not the direct analogue of the Hamilton and complex polar forms of a biquaternion. There are still two natural polar forms, but they are different in character:

1. **The idempotent polar form.** This form uses the idempotent decomposition and expresses the split quaternion as a pair of quaternion polar forms, one for each idempotent component.
2. **The exponential polar form.** This form uses the exponential of the split quaternion directly, and it involves both hyperbolic and trigonometric functions, depending on the sign of the split complex norm of the vector part.

These two forms are the subject of this article.

Throughout, we use the notation of the preceding articles: a split quaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3,
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The split complex unit is $j$, with $j^2 = +1$. The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The split complex conjugate is $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$. The Hermitian conjugate is $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$. The norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$.

The idempotents of the split complex algebra are $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split quaternion is

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

with $\tilde{Q}_\pm = \tilde{Q} e_\pm \in \mathbb{H}$ ordinary quaternions.

## The Idempotent Polar Form

### Definition

The **idempotent polar form** of a split quaternion $\tilde{Q}$ is the expression obtained by writing each idempotent component $\tilde{Q}_\pm$ in its quaternion polar form:

$$
\tilde{Q} = r_+ \exp(\mu_+ \theta_+) e_+ + r_- \exp(\mu_- \theta_-) e_-,
$$

where:

- $r_\pm = |\tilde{Q}_\pm| \geq 0$ is the ordinary quaternion modulus of $\tilde{Q}_\pm$;
- $\mu_\pm \in \mathbb{H}$ is a unit pure real quaternion (the **axis** of the component), defined when $\tilde{Q}_\pm$ has a nonzero vector part;
- $\theta_\pm \in \mathbb{R}$ is the **angle** of the component, defined by $\cos\theta_\pm = \Re(\tilde{Q}_\pm)/r_\pm$ and $\sin\theta_\pm = |\operatorname{Vec}(\tilde{Q}_\pm)|/r_\pm$.

The form is well-defined when both components are nonzero. If one component vanishes, the corresponding term is zero, and the form degenerates.

### The Quaternion Polar Form

Recall that every nonzero quaternion $q \in \mathbb{H}$ has a polar form

$$
q = r \exp(\mu\theta) = r(\cos\theta + \mu \sin\theta),
$$

where $r = |q| \geq 0$, $\mu$ is a unit pure real quaternion (the axis), and $\theta \in \mathbb{R}$ is the angle. The axis is defined when the vector part of $q$ is nonzero; when $q$ is a real scalar, the axis is undefined and the polar form reduces to $q = r$ (or $q = -r$, with $\theta = \pi$).

The idempotent polar form of a split quaternion is the extension of this to both components simultaneously.

### Properties

**Existence and uniqueness.** Every split quaternion $\tilde{Q}$ with both idempotent components nonzero has an idempotent polar form. The form is unique up to the sign ambiguities in each quaternion component: replacing $(r_\pm, \theta_\pm)$ by $(-r_\pm, \theta_\pm + \pi)$ gives the same $\tilde{Q}_\pm$.

**The moduli.** The moduli $r_\pm$ are non-negative real numbers. In the idempotent basis, the norm form is

$$
N(\tilde{Q}) = r_+^2 e_+ + r_-^2 e_-.
$$

So the two moduli are the square roots of the two components of the norm form in the idempotent basis.

**The angles.** The angles $\theta_\pm$ are real numbers, not complex. This is a significant simplification compared to the biquaternion case, where the angle in the Hamilton polar form is complex.

**The axes.** The axes $\mu_\pm$ are unit pure real quaternions. They are the analogues of the axis of a quaternion, and they lie in the unit sphere $\mathbb{S}^2$ in $\mathbb{R}^3$.

### The Case of Vanishing Components

If $\tilde{Q}_+ = 0$, the split quaternion $\tilde{Q}$ is a zero divisor (unless $\tilde{Q} = 0$), and the idempotent polar form degenerates: the first term vanishes, and the second term is the polar form of $\tilde{Q}_-$ alone:

$$
\tilde{Q} = r_- \exp(\mu_- \theta_-) e_-.
$$

If both components vanish, $\tilde{Q} = 0$ and the form is not defined.

### Why the Idempotent Polar Form Is Natural

The idempotent polar form is the natural polar form of a split quaternion because:

1. **It respects the semisimple structure.** The split quaternion algebra is the direct sum of two copies of the quaternion algebra, and the idempotent polar form treats each copy separately.
2. **It reduces to the quaternion polar form.** If the split quaternion lies in the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, then the two components are equal, $\tilde{Q}_+ = \tilde{Q}_- = q$, and the idempotent polar form reduces to the quaternion polar form $q = r \exp(\mu\theta)$ applied to each component.
3. **It has real angles.** Unlike the biquaternion case, the angles in the idempotent polar form are real numbers, not complex. This makes the form much easier to work with.
4. **It reveals the zero divisors.** The zero divisors are the elements with one component vanishing, and the idempotent polar form degenerates in exactly that case.

## The Exponential Polar Form

### Definition

The **exponential polar form** of a split quaternion is the expression obtained by computing the exponential of the split quaternion directly:

$$
\tilde{Q} = \exp(\tilde{L}),
$$

where $\tilde{L}$ is a split quaternion. This is the inverse of the logarithm, and it is the analogue of writing a complex number as $z = e^{w}$.

The exponential polar form is useful when the split quaternion is given as the exponential of another, and when the structure of the exponential is of interest.

### The Exponential of a Split Quaternion

Write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ where $Q_0 \in \mathbb{D}$ is the split scalar part and $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ is the split vector part. The scalar part commutes with everything, so

$$
\exp(\tilde{Q}) = \exp(Q_0 e_0) \exp(\mathbf{Q}) = e^{Q_0} \exp(\mathbf{Q}),
$$

where $e^{Q_0}$ is the split complex exponential and $\exp(\mathbf{Q})$ is the exponential of the vector part.

The split complex exponential is

$$
e^{Q_0} = e^{q_0} (\cosh q'_0 + j \sinh q'_0), \qquad Q_0 = q_0 + j q'_0.
$$

The exponential of the vector part depends on the split complex norm

$$
\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2},
$$

which is a split complex number in general.

### The Three Cases for the Vector Part

The exponential $\exp(\mathbf{Q})$ takes three different forms, depending on the sign of the real part of $\theta^2 = Q_1^2 + Q_2^2 + Q_3^2$.

**Case 1: $\theta^2$ positive real.** If $\theta^2 = r^2$ with $r > 0$ real, then

$$
\exp(\mathbf{Q}) = \cosh r \, e_0 + \frac{\sinh r}{r} \mathbf{Q}.
$$

This is the hyperbolic case. It occurs when the vector part has real components.

**Case 2: $\theta^2$ negative real.** If $\theta^2 = -r^2$ with $r > 0$ real, then

$$
\exp(\mathbf{Q}) = \cos r \, e_0 + \frac{\sin r}{r} \mathbf{Q}.
$$

This is the trigonometric case. It occurs when the vector part has purely split-imaginary components.

**Case 3: $\theta^2$ split complex.** If $\theta^2$ is a general split complex number, the exponential is expressed in terms of the split complex cosine and sine evaluated at $\theta$:

$$
\exp(\mathbf{Q}) = \cosh\theta \, e_0 + \frac{\sinh\theta}{\theta} \mathbf{Q},
$$

where $\cosh$ and $\sinh$ are the split complex hyperbolic functions. The formula is the same in all three cases; the three cases are distinguished by the sign of the real part of $\theta^2$.

So the exponential of a general split quaternion is

$$
\exp(\tilde{Q}) = e^{Q_0} \left(\cosh\theta \, e_0 + \frac{\sinh\theta}{\theta} \mathbf{Q}\right),
$$

where $\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$.

### The Nilpotent Case

If the vector part is nilpotent, i.e., if $\mathbf{Q}^2 = 0$, then $\theta = 0$ and the formula degenerates. In this case, $\exp(\mathbf{Q}) = e_0 + \mathbf{Q}$, as in the biquaternion case. But note: in the split quaternion algebra, the nilpotent vector parts are exactly the elements of the zero divisor subspaces $Z_\pm$ with vanishing scalar part. So the nilpotent case is more restricted than in the biquaternion case.

### The Exponential Polar Form

The exponential polar form of a split quaternion is obtained by inverting the exponential. The logarithm is multivalued, and the branches are determined by the branches of the split complex logarithm and the branches of the hyperbolic functions.

The principal branch of the logarithm is

$$
\log(\tilde{Q}) = \log(e^{Q_0}) e_0 + \log(\exp(\mathbf{Q})),
$$

where $\log(e^{Q_0})$ is the principal branch of the split complex logarithm and $\log(\exp(\mathbf{Q}))$ is computed from the inverse hyperbolic functions.

The exponential polar form is then

$$
\tilde{Q} = \exp(\log \tilde{Q}),
$$

which is the analogue of the polar form $z = r e^{i\theta}$ for a complex number.

### Why the Exponential Polar Form Is Useful

The exponential polar form is useful because:

1. **It connects to the differential operators.** The exponential is the solution of the scalar differential equation $\partial_0 \tilde{F} = \tilde{F}$, and the exponential polar form makes this transparent.
2. **It generalizes the complex polar form.** When the split quaternion is a split complex scalar, the exponential polar form reduces to the split complex polar form.
3. **It is the natural form for the analysis.** The exponential polar form is the form in which the split quaternion exponential appears in the solutions of the differential equations of the analysis.

## Comparison of the Two Polar Forms

The two polar forms are complementary, and they are used in different contexts.

| | Idempotent polar form | Exponential polar form |
|---|---|---|
| Based on | Idempotent decomposition | Exponential of the split quaternion |
| Modulus | Pair $(r_+, r_-)$ of non-negative reals | Split complex scalar $e^{Q_0}$ |
| Angle | Pair $(\theta_+, \theta_-)$ of real numbers | Split complex angle $\theta$ |
| Axis | Pair $(\mu_+, \mu_-)$ of unit pure real quaternions | Split vector direction |
| Reduces to | Quaternion polar form (in each component) | Split complex polar form (when $\mathbf{Q} = 0$) |
| Number of cases | One form | Three cases (hyperbolic, trigonometric, split) |
| Angles | Real | Split complex |

### When to Use Which

**Idempotent polar form.** Use this form when the algebra is viewed as the direct sum of two copies of the quaternion algebra, when the quaternion polar form is the natural language, and when the goal is to separate the two components.

**Exponential polar form.** Use this form when the exponential itself is the object of interest, when the split quaternion arises as the solution of a differential equation, and when the split complex structure is the natural language.

## Comparison with the Biquaternion Case

The polar representations of a split quaternion are significantly different from the polar representations of a biquaternion. The following table summarizes the differences.

| | $\mathbb{B}$ (biquaternion) | $\mathbb{H}_{\mathbb{D}}$ (split quaternion) |
|---|---|---|
| Extra unit | $i$, $i^2 = -1$ | $j$, $j^2 = +1$ |
| Number of polar forms | Two (Hamilton, complex) | Two (idempotent, exponential) |
| Nature of the forms | Both use roots of $-1$ | Idempotent uses the quaternion polar form; exponential uses the split complex exponential |
| Angles | Complex | Real (idempotent), split complex (exponential) |
| Modulus | Complex scalar (Hamilton), quaternion (complex) | Pair of reals (idempotent), split complex scalar (exponential) |
| Reduction to complex | Complex polar form | Split complex polar form |
| Reduction to quaternion | Hamilton polar form | Quaternion polar form (in each component) |

The key differences are:

1. **The split quaternion polar forms use the split complex structure, not the roots of $-1$.** The idempotent polar form uses the quaternion polar form in each component, and the exponential polar form uses the split complex exponential. Neither form uses the roots of $-1$ as a primary tool.

2. **The angles in the idempotent polar form are real numbers.** This is a significant simplification compared to the biquaternion case, where the angle in the Hamilton polar form is a complex number.

3. **The exponential polar form has three cases.** The hyperbolic case, the trigonometric case, and the general split case. In the biquaternion case, the exponential of the vector part always has the same form (the de Moivre formula with a complex angle).

4. **The idempotent polar form is the primary one.** In the biquaternion case, the primary polar form is the Hamilton form (or the complex form, depending on the context). In the split quaternion case, the primary form is the idempotent form, because it is the one that respects the semisimple structure.

## Behavior Under the Four Conjugations

The four conjugations of the split quaternion algebra act on the two polar forms as follows.

### Idempotent Polar Form

**Quaternion conjugation.** $\overline{r_\pm \exp(\mu_\pm \theta_\pm)} = r_\pm \exp(-\mu_\pm \theta_\pm)$, i.e., the sign of each angle is reversed.

**Split complex conjugation.** Swaps the two components, so $(r_+, \theta_+, \mu_+)$ and $(r_-, \theta_-, \mu_-)$ are exchanged.

**Hermitian conjugation.** Reverses the sign of each angle and swaps the two components.

**Anti-Hermitian conjugation.** The negative of the Hermitian conjugate.

### Exponential Polar Form

**Quaternion conjugation.** $\overline{\exp(\tilde{Q})} = \exp(\bar{\tilde{Q}})$ where $\bar{\tilde{Q}} = \bar{Q}_0 e_0 - \bar{\mathbf{Q}}$, i.e., the quaternion conjugate is applied to the argument.

**Split complex conjugation.** $(\exp(\tilde{Q}))^* = \exp(\tilde{Q}^*)$ where $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$, i.e., the split complex conjugate is applied to the argument.

**Hermitian conjugation.** $\exp(\tilde{Q})^\dagger = \exp(\tilde{Q}^\dagger)$ where $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$.

**Anti-Hermitian conjugation.** $\exp(\tilde{Q})^\flat = \exp(\tilde{Q}^\flat)$ where $\tilde{Q}^\flat = -\tilde{Q}^\dagger$.

So the exponential polar form behaves simply under the four conjugations: each conjugation is applied to the argument of the exponential, and the exponential is preserved. This is a significant simplification compared to the biquaternion case, where the conjugation of the polar form involves conjugating the modulus, the angle, and the root.

## Applications

### The Rotation Analogy

In the quaternion algebra, a unit quaternion $\exp(\mu\theta/2)$ acts on a pure quaternion by conjugation, giving a rotation. In the split quaternion algebra, the same construction gives a rotation in the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$. So the idempotent polar form can be used to compute rotations in each copy of the quaternion algebra separately.

### The Boost Analogy

The split quaternion algebra contains elements whose exponential gives a boost (a hyperbolic rotation). These are the elements with a real vector part and vanishing scalar part, for which the exponential is the hyperbolic case. The boost analogy is one of the reasons the split quaternion algebra appears in relativistic physics.

### The Exponential in the Analysis

The exponential polar form is the natural form for the analysis of functions of a split quaternion variable. The exponential is the solution of the differential equation $\partial_0 \tilde{F} = \tilde{F}$, and the polar form makes the structure of the solutions transparent.

## Open Questions

1. **Convergence of the exponential polar form.** Under what conditions does the exponential polar form converge, and what is its domain of definition?

2. **Relation between the two polar forms.** Is there a transformation that maps the idempotent polar form to the exponential polar form, or are they independent?

3. **The analogue of the polar decomposition of matrices.** Is there an analogue of the polar decomposition for split quaternions, and what would it look like?

4. **The role of the roots of $-1$.** The roots of $-1$ in the split quaternion algebra are a four-dimensional family, but they are not used in the polar forms as they are in the biquaternion case. What is the role of the roots of $-1$ in the split quaternion polar representations?

5. **Behavior under the analysis.** How do the two polar forms interact with the differential operators of the analysis? In particular, what is the gradient of a split quaternion in polar form?

6. **Application to signal processing.** Can the split quaternion polar forms be used in signal processing, as the biquaternion polar forms are used in the discrete and continuous harmonic analysis?

## Summary

The split quaternion algebra has two natural polar representations:

**The idempotent polar form.** Every split quaternion with both idempotent components nonzero is written as

$$
\tilde{Q} = r_+ \exp(\mu_+ \theta_+) e_+ + r_- \exp(\mu_- \theta_-) e_-,
$$

where $r_\pm \geq 0$ are the quaternion moduli of the two components, $\mu_\pm$ are unit pure real quaternions (the axes), and $\theta_\pm$ are real numbers (the angles). This form is the natural polar form of the split quaternion algebra, because it respects the semisimple structure and reduces to the quaternion polar form in each component. The angles are real numbers, which is a simplification compared to the biquaternion case.

**The exponential polar form.** Every split quaternion with nonzero norm form is written as $\tilde{Q} = \exp(\tilde{L})$, where $\tilde{L}$ is a split quaternion. The exponential of a general split quaternion is

$$
\exp(\tilde{Q}) = e^{Q_0} \left(\cosh\theta \, e_0 + \frac{\sinh\theta}{\theta} \mathbf{Q}\right),
$$

where $\theta = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$. The form has three cases: hyperbolic (when $\theta^2$ is positive real), trigonometric (when $\theta^2$ is negative real), and general split (when $\theta^2$ is a general split complex number).

The two polar forms are complementary. The idempotent polar form is the primary one, because it reveals the structure of the algebra. The exponential polar form is useful in the analysis, where the exponential is the fundamental solution of the scalar differential equation.

The polar representations of a split quaternion are different in character from the polar representations of a biquaternion. In the biquaternion case, the two polar forms both use the roots of $-1$, and the angles are complex. In the split quaternion case, the idempotent form uses the quaternion polar form in each component, and the exponential form uses the split complex exponential. The angles are real (idempotent form) or split complex (exponential form), and the roots of $-1$ play a lesser role.

The simplification is a reflection of the fact that the split quaternion algebra is semisimple, while the biquaternion algebra is simple. The semisimple structure is what makes the idempotent polar form the natural one, and it is what makes the invertibility criterion linear and the zero divisor set a union of linear subspaces.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation of quaternions.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the polar representations of split quaternions and biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.

