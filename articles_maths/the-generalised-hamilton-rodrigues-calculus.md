# __The Generalised Hamilton–Rodrigues Calculus__

## Introduction

Quaternion analysis has two classical notions of differentiability, and both are too restrictive for the calculus of a quaternion-valued function that is not already a function of one complex direction. The difference quotient of the naive definition exists only for affine functions, and the Cauchy–Riemann–Fueter condition admits only the regular functions; neither class contains $\tilde q\mapsto\tilde q^2$, and neither is closed under the operations by which an estimation is carried out. This article develops the third notion, the **generalised Hamilton–Rodrigues calculus**, in which the derivative of $f$ with respect to the conjugate is a fixed real-linear combination of the four real partial derivatives of $f$. The derivative then exists for every differentiable $f$, it is a quarter of the Fueter operator, it vanishes exactly on the left-regular functions, and it carries the rules — behaviour under a constant multiple, a product rule with a change of variable, a chain rule, a real-valued chain rule, a descent direction — that an optimisation needs.

Four boundaries are held.

- The difference quotient, its failure, and the Cauchy–Riemann–Fueter condition for the quaternion algebra are those of *Quaternion Analysis*; the general statement that a difference-quotient derivative is over-determined once the ground algebra is not a field is that of *Hypercomplex Analysis*. The operator $D = \sum_\mu e_\mu\partial_\mu$, its conjugate, the regular functions it annihilates, their harmonicity and the ellipticity of the equation are those of *Fueter Theory for Quaternions*, of *Quaternion Regular Functions* and of *Regularity and the Cauchy–Riemann Operator*. None of them is restated here.
- The real differential calculus that the definition uses — the Fréchet derivative, the partial derivatives, the total derivative and the chain rule for a map between open sets of $\mathbb{R}^n$ — is that of *Differential Calculus on Normed Spaces*. The four partial derivatives below are the four derivatives in the basis directions, and no other calculus is invoked.
- The involutions $\iota_k$ about the coordinate axes, the Klein group they form and the sign matrix of the family are those of the companion article *Quaternion Augmented Statistics*; the same article uses the four augmented derivatives below in the least-squares solution of a widely linear estimator, which is the reason the calculus was built. The inner automorphism $\iota_u$ itself is from *Quaternion Automorphisms and Derivations*.
- The Cauchy kernel, its regularity and the integral formula that uses it are *Quaternion Integration*. The calculus here is differential and local, and no integral is taken.

No physics is invoked.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$; a quaternion is $\tilde q = \sum_\mu q_\mu e_\mu$, its conjugate is $\tilde{q}^{\natural} = \tilde{q}^{*} = q_0-\mathbf{q}$, its quaternion norm is $N(\tilde q) = \tilde q\tilde{q}^{\natural} = \sum_\mu q_\mu^2$, its modulus is $|\tilde q| = \sqrt{N(\tilde q)}$, and $\mathrm{Sc}(\tilde q) = q_0$ and $\mathbf{q} = \sum_k q_ke_k$ are the scalar and vector parts. The conjugates of the units are $e_0^{\natural} = e_0$ and $e_k^{\natural} = -e_k$. For $f$ on an open $\Omega\subseteq\mathbb{H}$ the four **partial derivatives** are $\partial_\mu f = \frac{d}{dt}\big|_{t=0}f(\tilde q+te_\mu)$, each quaternion valued, and $f$ is differentiable when they exist and are continuous, the algebra being identified with $\mathbb{R}^4$. The involutions about the axes are $\iota_0 = \mathrm{id}$ and $\iota_k(\tilde q) = e_k\tilde q e_k^{-1}$, with $\iota_j\iota_m = \iota_{j\oplus m}$ and $\iota_k(e_\mu) = \sigma_{k\mu}e_\mu$.

## What the Classical Notions Give

### The Difference Quotient

**Theorem (from the classical theory).** A function whose difference quotient $(f(\tilde q+h)-f(\tilde q))h^{-1}$ tends to a limit independently of the direction of the approach $h\to0$ is forced to be affine; the class of such functions is too small to carry an analysis, and it does not contain $\tilde q\mapsto\tilde q^2$.

*Proof.* This is the theorem of *Quaternion Analysis*: the limit is required along every path, the four coordinate directions and the two-sided paths among them, and those requirements are together incompatible with a non-affine $f$. The failure for $\tilde q^2$ is computed in the same article.

### The Cauchy–Riemann–Fueter Condition

**Definition.** A differentiable $f$ is **left-regular**, or **monogenic**, when $Df = 0$ for the Fueter operator $D = \sum_\mu e_\mu\partial_\mu$, and **right-regular** when $fD = \sum_\mu\partial_\mu f\,e_\mu = 0$.

Regularity is the correct replacement of holomorphy: the equation is elliptic, its solutions are harmonic, they carry a Cauchy integral formula, and they form a right $\mathbb{H}$-module. The class is nevertheless too small for the calculus of an arbitrary differentiable function. It contains the constants, the single-plane holomorphic functions and the Cauchy kernel; it does not contain $\tilde q$ or $\tilde q^2$, and it is not closed under left multiplication by a general constant.

### What Is Needed Instead

An optimisation of a quaternion-valued function of a quaternion variable needs three things of a derivative: that it exist for every differentiable function of interest; that it carry the rate of change along each real direction; and that it give a direction of steepest change and a descent step. Regularity provides the second and the third only for its own functions, and the difference quotient provides none of them. The generalised Hamilton–Rodrigues calculus takes the four real partial derivatives, which exist for every differentiable $f$, and packages them into four fixed combinations that are the derivatives of $f$ with respect to the four conjugate variables.

## The Derivative with Respect to the Conjugate

### The Definition

**Definition.** For a differentiable $f : \Omega\to\mathbb{H}$ the **derivative with respect to the conjugate** and the **derivative with respect to the variable** are

$$
\frac{\partial f}{\partial\bar{\tilde{q}}} = \frac14\sum_{\mu=0}^{3}e_\mu\,\partial_\mu f , \qquad \frac{\partial f}{\partial\tilde q} = \frac14\sum_{\mu=0}^{3}e_\mu^{\natural}\,\partial_\mu f .
$$

The names are names of operators and not limits: there is no difference quotient, and each derivative is a fixed real-linear combination of the four partial derivatives. The two are related by

$$
\frac{\partial f}{\partial\tilde q} = (\ \frac{\partial \bar f}{\partial\bar{\tilde{q}}}\ )^{\natural} ,
$$

since $\partial_\mu\bar f = \overline{\partial_\mu f}$ and $e_\mu^{\natural} = \overline{e_\mu}$.

**Remark (the complex case that is generalised).** In the complex case the same construction reads $\partial/\partial A = \frac12(\partial_a-i\partial_{a'})$ and $\partial/\partial \bar{A} = \frac12(\partial_a+i\partial_{a'})$, the factor being $\frac12$ in a two-dimensional algebra and the sign being the sign of $\bar i = -i$; a holomorphic function is one with $\partial f/\partial \bar{A} = 0$, and the operator exists for every differentiable $f$ but agrees with the holomorphic derivative only on that class. The quaternion calculus keeps the factor $\frac14$ and the signs of the three imaginary units, so it is the same construction on the four-dimensional algebra. What it does not keep is the vanishing of $\partial\tilde q/\partial\bar{\tilde{q}}$: the four partials of $\tilde q$ are the four units $e_0,e_1,e_2,e_3$, which are linearly independent, so no non-zero constant-coefficient operator in the partials annihilates $\tilde q$. No function of $\tilde q$ alone is therefore annihilated by the conjugate derivative, and the analogy with holomorphy is not what the calculus delivers.

### The Fueter Reading

**Theorem.** With $D = \sum_\mu e_\mu\partial_\mu$ the Fueter operator and $\bar D = \sum_\mu e_\mu^{\natural}\partial_\mu$ its conjugate,

$$
\frac{\partial f}{\partial\bar{\tilde{q}}} = \frac14 Df , \qquad \frac{\partial f}{\partial\tilde q} = \frac14\bar Df .
$$

Consequently $f$ is left-regular if and only if $\partial f/\partial\bar{\tilde{q}} = 0$, and $f$ is right-regular if and only if the left derivative defined below vanishes, $\frac14\sum_\mu\partial_\mu f\,e_\mu = 0$.

*Proof.* The two operators are the two definitions, together with $D = \sum_\mu e_\mu\partial_\mu$ and $\bar D = \sum_\mu e_\mu^{\natural}\partial_\mu$ of *Fueter Theory for Quaternions*. The two statements about regularity restate the definitions.

**Remark.** The calculus is the differential calculus of the Fueter operator applied to functions that are not regular: the conjugate derivative measures the failure of left regularity, and its vanishing is exactly the regularity that *Quaternion Regular Functions* develops. Its value is that it exists outside that class, where the Cauchy integral formula and the module structure do not apply.

### The Four Augmented Derivatives

**Definition.** For $j = 0,1,2,3$ the **augmented derivatives** are

$$
\frac{\partial f}{\partial\bar{\tilde{q}_j}} = \frac14\sum_{\mu=0}^{3}\iota_j(e_\mu)\,\partial_\mu f ,
$$

with $\iota_0 = \mathrm{id}$, so that the case $j = 0$ is $\partial f/\partial\bar{\tilde{q}}$. In coordinates $\iota_j(e_\mu) = \sigma_{j\mu}e_\mu$ and the definition reads $\frac14\sum_\mu\sigma_{j\mu}e_\mu\partial_\mu f$.

**Proposition.** The augmented derivative is the conjugate derivative of $f$ read in the involuted variable,

$$
\frac{\partial f}{\partial\bar{\tilde{q}_j}}(\tilde q) = \frac{\partial(f\circ\iota_j)}{\partial\bar{\tilde{q}}}\bigl(\iota_j\tilde q\bigr) , \qquad j = 0,1,2,3 .
$$

*Proof.* The map $\iota_j$ is linear with $\iota_j^{-1} = \iota_j$ and replaces the direction $e_\mu$ by the direction $\iota_j(e_\mu) = \sigma_{j\mu}e_\mu$; by the chain rule for a linear change of variable, the conjugate derivative of $f\circ\iota_j$ at the point $\iota_j\tilde q$ is the combination $\frac14\sum_\mu\sigma_{j\mu}e_\mu\partial_\mu f$ of the partials of $f$ at $\tilde q$, which is the definition.

**Example.** The four augmented derivatives of the square are

$$
\frac{\partial \tilde q^2}{\partial\bar{\tilde{q}_1}} = \tilde q-q_1e_1 , \qquad \frac{\partial \tilde q^2}{\partial\bar{\tilde{q}_2}} = \tilde q-q_2e_2 , \qquad \frac{\partial \tilde q^2}{\partial\bar{\tilde{q}_3}} = \tilde q-q_3e_3 ,
$$

while $\frac{\partial \tilde q^2}{\partial\bar{\tilde{q}}} = -\mathrm{Sc}(\tilde q)$. The computation is direct from $\partial_\mu(\tilde q^2) = e_\mu\tilde q+\tilde qe_\mu$, and it shows the pattern: the involution $j$ removes the $e_j$-component from the value, and the case $j = 0$ is different in kind, because the identity is not one of the three rotations but the sum of the other three and the conjugate.

**Remark.** The four operators have constant coefficients and therefore commute with one another, $\frac{\partial}{\partial\bar{\tilde{q}_j}}\frac{\partial f}{\partial\bar{\tilde{q}_m}} = \frac{\partial}{\partial\bar{\tilde{q}_m}}\frac{\partial f}{\partial\bar{\tilde{q}_j}}$ for $C^2$ functions; consequently every rule below iterates to higher order. The calculus is a calculus of the second order as well, the second derivatives being the four-by-four array $\partial_\mu\partial_\nu f$ read in the two involution frames.

### The Failure of the Naive Leibniz Rule

**Proposition.** The conjugate derivative is $\mathbb{R}$-linear and left linear over the constants on the right: $\frac{\partial(fc)}{\partial\bar{\tilde{q}}} = \frac{\partial f}{\partial\bar{\tilde{q}}}c$ for every constant $c$. It is not a derivation of the algebra: the naive Leibniz rule

$$
\frac{\partial(fp)}{\partial\bar{\tilde{q}}} = \frac{\partial f}{\partial\bar{\tilde{q}}}\,p+f\,\frac{\partial p}{\partial\bar{\tilde{q}}}
$$

fails.

*Proof.* Linearity in $f$ is the linearity of the partial derivatives. For the constant on the right, $\partial_\mu(fc) = (\partial_\mu f)c$ because $c$ is constant, and $c$ may be taken out of the sum. For the failure, take $f = p = \tilde q$: the naive rule gives $-\frac12\tilde q-\frac12\tilde q = -\tilde q$ at every point, while the direct value of $\frac{\partial\tilde q^2}{\partial\bar{\tilde{q}}}$ is $-\mathrm{Sc}(\tilde q)$, and the two differ at every point whose scalar part does not vanish. The correct rule is the product rule below, in which the derivative of the right factor is taken in a variable moved by an inner automorphism determined by the left factor.

### The Left Derivative

**Definition.** The **left derivative** is

$$
\frac{\partial^{\mathrm{L}}f}{\partial\bar{\tilde{q}}} = \frac14\sum_{\mu=0}^{3}\partial_\mu f\,e_\mu ,
$$

with the imaginary units on the right of the partials.

**Remark.** The two operators agree on the identity, on the conjugate and on the square, but they are different. For $f(\tilde q) = \tilde qe_1$ one has $\frac{\partial^{\mathrm{L}}f}{\partial\bar{\tilde{q}}} = \frac12e_1$, since $\sum_\mu e_\mu e_1e_\mu = 2e_1$, while $\frac{\partial f}{\partial\bar{\tilde{q}}} = -\frac12e_1$, since $\sum_\mu e_\mu e_\mu e_1 = -2e_1$. The left derivative is the natural one for functions whose coefficients are written on the right, and it is the operator whose vanishing is right regularity. Every statement below has its left counterpart, obtained by moving the constant factors to the other side.

## Base Cases

**Proposition.** The derivatives of the elementary functions are as follows.

| $f(\tilde q)$ | $\dfrac{\partial f}{\partial\tilde q}$ | $\dfrac{\partial f}{\partial\bar{\tilde{q}}}$ |
|---|---|---|
| $\tilde q$ | $1$ | $-\tfrac12$ |
| $\tilde{q}^{\natural}$ | $-\tfrac12$ | $1$ |
| $N(\tilde q) = \tilde q\tilde{q}^{\natural}$ | $\tfrac12\tilde{q}^{\natural}$ | $\tfrac12\tilde q$ |
| $\lvert\tilde q\rvert$ | $\dfrac{\tilde{q}^{\natural}}{4\lvert\tilde q\rvert}$ | $\dfrac{\tilde q}{4\lvert\tilde q\rvert}$ |
| $\tilde q^2$ | $\tilde q+\mathrm{Sc}(\tilde q)$ | $-\mathrm{Sc}(\tilde q)$ |
| $\dfrac{\tilde{q}^{\natural}}{N(\tilde q)^2}$ | not identically zero | $0$ |

*Proof.* The first two rows are the sums $\sum_\mu e_\mu e_\mu = \sum_\mu e_\mu^{\natural} e_\mu^{\natural} = -2$ and $\sum_\mu e_\mu e_\mu^{\natural} = \sum_\mu e_\mu^{\natural} e_\mu = 4$, applied to $\partial_\mu\tilde q = e_\mu$ and $\partial_\mu\tilde{q}^{\natural} = e_\mu^{\natural}$. For the norm and the modulus the partials $\partial_\mu N = 2q_\mu$ and $\partial_\mu|\tilde q| = q_\mu/|\tilde q|$ are real, so the combination $\frac14\sum_\mu e_\mu\partial_\mu$ of a real-valued function is the vector of its gradient, and the two displayed values follow by reading the gradient as the quaternion $\sum_\mu(\partial_\mu f)e_\mu$. For the square one uses $\partial_\mu(\tilde q^2) = e_\mu\tilde q+\tilde qe_\mu$ together with $\sum_\mu e_\mu\tilde qe_\mu = -2\tilde{q}^{\natural}$ and $\sum_\mu e_\mu^{\natural}\tilde qe_\mu = 4\mathrm{Sc}(\tilde q)$, the second of these because $e_k^{\natural}\tilde qe_k = \iota_k\tilde q$ and $\tilde q+\iota_1\tilde q+\iota_2\tilde q+\iota_3\tilde q = \tilde q+2\tilde{q}^{\natural}+\tilde q$. For the last row, the function is the Cauchy kernel $E$ of *Quaternion Integration*, which is left-regular, so its conjugate derivative vanishes by the Fueter reading and its other derivative does not, by the relation between the two derivatives applied to $\bar E = \tilde q/N(\tilde q)^2$, whose conjugate derivative is not zero either.

The three functions $N$, $|\tilde q|$ and $E$ are the ones that appear as a cost and as a kernel; the two rows $\tilde q$ and $\tilde{q}^{\natural}$ are the ones that show the failure of the naive rules, the conjugate derivative of the identity being $-\frac12$ rather than $0$.

## The Rules

### Constant Multiples

**Proposition.** Let $\nu\in\mathbb{H}$, $\nu\neq0$, and let $f$ be differentiable. Then

$$
\frac{\partial(\nu f)}{\partial\bar{\tilde{q}}}(\tilde q) = \nu\,\frac{\partial f_\star}{\partial \tilde q_\star^*}\Big|_{\tilde q_\star = \iota_{\nu^{-1}}\tilde q} , \qquad f_\star(\tilde q_\star) = f(\tilde q) ,
$$

the derivative of $f$ being taken in the variable $\tilde q_\star = \iota_{\nu^{-1}}\tilde q$ obtained from $\tilde q$ by the inner automorphism determined by $\nu$. When $\nu$ is real, $\iota_{\nu^{-1}} = \mathrm{id}$ and the rule is the naive one, $\frac{\partial(\nu f)}{\partial\bar{\tilde{q}}} = \nu\frac{\partial f}{\partial\bar{\tilde{q}}}$; when $\nu$ is purely imaginary the change of variable is the involution about the axis of $\nu$, and the naive rule fails.

*Proof.* For a constant $\nu$, $\partial_\mu(\nu f) = \nu\,\partial_\mu f$, so $\frac{\partial(\nu f)}{\partial\bar{\tilde{q}}} = \frac14\sum_\mu e_\mu\nu\,\partial_\mu f$. On the other side, $\frac14\sum_\mu e_\mu\nu\,\partial_\mu f = \frac14\nu\sum_\mu\nu^{-1}e_\mu\nu\,\partial_\mu f = \nu\cdot\frac14\sum_\mu\iota_{\nu^{-1}}(e_\mu)\partial_\mu f$, and the last factor is the conjugate derivative of $f$ read in the variable $\iota_{\nu^{-1}}\tilde q$, by the same chain-rule argument as for the augmented derivatives. The claim about a real $\nu$ is the centrality of a real number; the failure for a purely imaginary $\nu$ is the non-commutation of $\nu$ with the units in the first sum, and it is visible already on $\tilde q^2$.

**Proposition (constant on the right).** For a constant $\nu$, $\frac{\partial(f\nu)}{\partial\bar{\tilde{q}}} = \frac{\partial f}{\partial\bar{\tilde{q}}}\nu$, with no change of variable.

*Proof.* $\partial_\mu(f\nu) = (\partial_\mu f)\nu$ and $\nu$ may be taken out of the sum on the right of the units.

### The Product Rule

**Theorem.** Let $f,p$ be differentiable with $f(\tilde q)\neq0$. Then

$$
\frac{\partial(fp)}{\partial\bar{\tilde{q}}}(\tilde q) = \frac{\partial f}{\partial\bar{\tilde{q}}}(\tilde q)\,p(\tilde q)+f(\tilde q)\,\frac{\partial p_\star}{\partial\tilde q_\star^*}\Big|_{\tilde q_\star = \iota_{f(\tilde q)^{-1}}\tilde q} ,
$$

where $p_\star(\tilde q_\star) = p(\tilde q)$.

*Proof.* The partial derivatives of a product are $\partial_\mu(fp) = (\partial_\mu f)p+f\,\partial_\mu p$, so

$$
\frac{\partial(fp)}{\partial\bar{\tilde{q}}} = \Bigl(\frac14\sum_\mu e_\mu\partial_\mu f\Bigr)p+\frac14\sum_\mu e_\mu f\,\partial_\mu p ,
$$

the first term being the product of the derivative of $f$ with $p$. In the second term the constant $f(\tilde q)$ is carried out of the sum on the left and the remaining combination $\frac14\sum_\mu e_\mu\partial_\mu p$ is the conjugate derivative of $p$ read in the variable moved by $\iota_{f(\tilde q)^{-1}}$, by the same argument as for the constant multiples.

**Remark.** The two terms are the two terms of the Leibniz rule, the first with $p$ held constant and the second with $f$ held constant, and the second differs from $f\frac{\partial p}{\partial\bar{\tilde{q}}}$ by the change of variable, which is the identity exactly when $f(\tilde q)$ is central, that is when the factor $f$ is real valued. The rule reduces to the naive one on every real-valued factor, and it is naive-plus-a-rotation otherwise.

**Example (consistency with the squared norm).** For the product $\tilde q\tilde{q}^{\natural}$ the second term of the product rule is the derivative of the conjugate in the variable moved by $\iota_{\tilde{q}^{\natural}}$, and the value of the sum is $\frac12\tilde q$, which is the direct value of the third row of the table. The consistency is a check on the change of variable: the naive rule would give $-\frac12\tilde{q}^{\natural}+\tilde q$, which agrees with the true value only where $\tilde q$ is real.

### The Chain Rule

**Theorem.** Let $p$ be differentiable and let $g$ be differentiable on a neighbourhood of $p(\Omega)$, with $p_\nu$ the $e_\nu$-component of $p$. Then

$$
\frac{\partial(g\circ p)}{\partial\bar{\tilde{q}}}(\tilde q) = \frac14\sum_{\mu,\nu=0}^{3}e_\mu\,(\partial_\nu g)\bigl(p(\tilde q)\bigr)\,\partial_\mu p_\nu(\tilde q) .
$$

*Proof.* The chain rule of *Differential Calculus on Normed Spaces* gives $\partial_\mu(g\circ p)(\tilde q) = \sum_\nu(\partial_\nu g)(p(\tilde q))\,\partial_\mu p_\nu(\tilde q)$, the derivative of $g$ at $p(\tilde q)$ being applied to the vector $\partial_\mu p$, whose coordinates in the basis are $\partial_\mu p_\nu$. Multiplying by $e_\mu$ and summing over $\mu$ with the factor $\frac14$ is the definition.

**Corollary (a real-valued inner function).** If $p$ is real valued and $g : \mathbb{R}\to\mathbb{R}$ is differentiable, then $g\circ p$ is real valued and

$$
\frac{\partial(g\circ p)}{\partial\bar{\tilde{q}}} = \frac{\partial p}{\partial\bar{\tilde{q}}}\,g'(p) .
$$

*Proof.* For a real-valued $p$ the only non-vanishing coordinate is $p_0$, so the chain rule collapses to $\frac14\sum_\mu e_\mu(\partial_0g)(p)\partial_\mu p$, and $(\partial_0g)(p) = g'(p)$ is a real scalar, which commutes with the units and may be moved to the right.

**Example.** For the modulus, which is the composition of the norm with the square root, the corollary gives $\frac{\partial|\tilde q|}{\partial\bar{\tilde{q}}} = \frac{\partial N}{\partial\bar{\tilde{q}}}\cdot\frac{1}{2\sqrt{N}}$ with $\frac{\partial N}{\partial\bar{\tilde{q}}} = \frac12\tilde q$, which is $\tilde q/(4|\tilde q|)$, the fourth row of the table.

### The Direction of Steepest Change

**Definition.** For a real-valued differentiable $J$ and a direction $r\in\mathbb{H}$ the **directional derivative** is $J'(\tilde q;r) = \frac{d}{dt}\big|_{t=0}J(\tilde q+tr)$.

**Proposition.** For real-valued $J$ the conjugate derivative is a quarter of the gradient, $\frac{\partial J}{\partial\bar{\tilde{q}}} = \frac14\nabla J$ with $\nabla J = \sum_\mu(\partial_\mu J)e_\mu$ read as a quaternion, and

$$
J'(\tilde q;r) = \bigl\langle r,\nabla J(\tilde q)\bigr\rangle = 4\,\Bigl\langle r,\frac{\partial J}{\partial\bar{\tilde{q}}}\Bigr\rangle .
$$

Consequently $\frac{\partial J}{\partial\bar{\tilde{q}}}$ points along the direction of steepest ascent, the rate there being $|\nabla J(\tilde q)|$, and $-\frac{\partial J}{\partial\bar{\tilde{q}}}$ is a descent direction for $J$.

*Proof.* The directional derivative is the inner product of the direction with the gradient, by the real differentiability of $J$; the conjugate derivative $\frac14\sum_\mu e_\mu\partial_\mu J$ is the same quaternion as the gradient $\sum_\mu(\partial_\mu J)e_\mu$, since the coefficients are real and the two orderings agree. The rate of increase is the inner product with the unit vector $\nabla J/|\nabla J|$, which is $|\nabla J|$, and it is attained in the direction of the gradient, hence in the direction of $\frac{\partial J}{\partial\bar{\tilde{q}}}$; the sign reversal gives the descent statement.

**Remark.** The proposition is the reason the calculus is the one an estimation uses: a gradient step on a real-valued cost is a subtraction of a multiple of the conjugate derivative, the multiple being the step size, and the calculus is closed under the composition of the steps because the four derivatives commute and the rules above are stated for every differentiable function. The companion article *Quaternion Augmented Statistics* uses the derivative in the least-squares solution of a widely linear estimator, where the normal equations are the orthogonality conditions of the same projection.

## Summary

The naive difference-quotient derivative of a quaternion-valued function exists only for affine functions, and the Cauchy–Riemann–Fueter condition admits only the regular functions; neither class contains $\tilde q^2$. The generalised Hamilton–Rodrigues calculus replaces the limit by a fixed combination of the four real partial derivatives, $\frac{\partial f}{\partial\bar{\tilde{q}}} = \frac14\sum_\mu e_\mu\partial_\mu f$ and $\frac{\partial f}{\partial\tilde q} = \frac14\sum_\mu e_\mu^{\natural}\partial_\mu f$, defined for every differentiable $f$; the first is a quarter of the Fueter operator and the second a quarter of its conjugate, so the first vanishes exactly on the left-regular functions, and the operator with the units on the right vanishes exactly on the right-regular ones. The construction generalises the complex operators $\frac12(\partial_a\mp i\partial_{a'})$ but not the vanishing of $\partial A/\partial \bar{A}$, because the four partials of $\tilde q$ are independent; no class is picked out by the vanishing of a derivative of the first variable alone.

The four augmented derivatives $\frac{\partial f}{\partial\bar{\tilde{q}_j}} = \frac14\sum_\mu\iota_j(e_\mu)\partial_\mu f$ are the conjugate derivatives read in the four involuted variables, so the calculus and the augmented statistics of the companion article are the same device seen twice. The rules are: linearity and left linearity over constants on the right; the base values $\partial\tilde q/\partial\bar{\tilde{q}} = -\frac12$, $\partial\tilde{q}^{\natural}/\partial\bar{\tilde{q}} = 1$, $\partial N/\partial\bar{\tilde{q}} = \frac12\tilde q$, $\partial|\tilde q|/\partial\bar{\tilde{q}} = \tilde q/(4|\tilde q|)$, $\partial\tilde q^2/\partial\bar{\tilde{q}} = -\mathrm{Sc}(\tilde q)$ and $\frac{\partial}{\partial\bar{\tilde{q}}}(\tilde{q}^{\natural}/N^2) = 0$; a constant multiple rule in which the derivative is taken in the variable moved by an inner automorphism, trivial for a real factor and non-trivial otherwise; a product rule whose second term carries the same change of variable determined by the left factor; a chain rule that is the real chain rule read in the basis; a real-valued chain rule $\frac{\partial(g\circ p)}{\partial\bar{\tilde{q}}} = \frac{\partial p}{\partial\bar{\tilde{q}}}g'(p)$; and the descent statement, that $-\frac{\partial J}{\partial\bar{\tilde{q}}}$ decreases a real-valued $J$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\partial_\mu f$ | Partial derivative in the direction $e_\mu$, $\partial_\mu f = \frac{d}{dt}\big|_{t=0}f(\tilde q+te_\mu)$ |
| $\dfrac{\partial f}{\partial\bar{\tilde{q}}} = \frac14\sum_\mu e_\mu\partial_\mu f$ | Derivative with respect to the conjugate; $\frac14 Df$ |
| $\dfrac{\partial f}{\partial\tilde q} = \frac14\sum_\mu e_\mu^{\natural}\partial_\mu f$ | Derivative with respect to the variable; $\frac14\bar Df$ |
| $D = \sum_\mu e_\mu\partial_\mu$, $\bar D$ | Fueter operator and its conjugate, of *Fueter Theory for Quaternions* |
| $\dfrac{\partial f}{\partial\bar{\tilde{q}_j}} = \frac14\sum_\mu\iota_j(e_\mu)\partial_\mu f$ | The four augmented derivatives; $j = 0$ is $\partial f/\partial\bar{\tilde{q}}$ |
| $\iota_j$, $\sigma_{j\mu}$ | Involutions about the axes and their sign matrix, of *Quaternion Augmented Statistics* |
| $\dfrac{\partial^{\mathrm{L}}f}{\partial\bar{\tilde{q}}} = \frac14\sum_\mu\partial_\mu f\,e_\mu$ | Left derivative, with the units on the right |
| $\iota_{\nu^{-1}}(\tilde q) = \nu^{-1}\tilde q\nu$ | Change of variable in the constant-multiple and product rules |
| $\nabla J = \sum_\mu(\partial_\mu J)e_\mu$ | Gradient of a real-valued $J$; $\frac{\partial J}{\partial\bar{\tilde{q}}} = \frac14\nabla J$ |

## Further Reading

- Dongpo Xu, Claudio Jahanchahi, Clive Cheong Took and Danilo P. Mandic, "Enabling quaternion derivatives: the generalized HR calculus", *Royal Society Open Science* **2** (2015), 150255, for the calculus as it was introduced.
- Danilo P. Mandic and Vanessa Su Lee Goh, *Complex Valued Nonlinear Adaptive Filters: Noncircularity, Widely Linear and Neural Models* (Wiley, 2009), for the CR-calculus, the complex case of the same construction.
- Ken Kreutz-Delgado, "The complex gradient operator and the CR-calculus" (2006), for the derivation of the complex rules by the same device.
- Anthony Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979), 199–225, for the analysis of the regular functions.
- Klaus Gürlebeck and Wolfgang Sprössig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the Fueter operator, its fundamental solution and the integral formulae.
- Fabrizio Colombo, Irene Sabadini and Daniele C. Struppa, *Noncommutative Functional Calculus* (Birkhäuser, 2011), for the other calculus of quaternion-valued functions, the slice one, and its relation to the regular functions.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the algebra.
