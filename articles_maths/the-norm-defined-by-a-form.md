# __The Norm Defined by a Form__

## Introduction

A positive definite Hermitian form on a sesqualgebra is a length. The diagonal $h(x,x)$ of such a form lies in the fixed field $k = R^{\varsigma}$ of the base involution, it is positive for $x \neq 0$, and its square root is a **norm** on the module,

$$
\|x\| = h(x,x)^{1/2} .
$$

The norm is read from the diagonal alone, and with it the pair $(A,h)$ becomes a normed space on which the form is bounded: the **Cauchy–Schwarz inequality** $\lvert h(x,y)\rvert \leq \|x\|\|y\|$ is a consequence of the definiteness and not a hypothesis, the triangle inequality follows from it, and the form is continuous for the topology the norm defines. When in addition the norm is submultiplicative the object is a **normed sesqualgebra with a form**, complete exactly when it is a **Banach sesqualgebra with a form**, and the compatibility of *Topological Sesqualgebras with a Form*, §*The Compatibility*, then says that the one-sided multiplications come in adjoint pairs that the norm bounds.

Three facts organise the article. **The definite diagonal is a positive square.** The diagonal takes its values in the fixed field $k$, and it is positive away from zero exactly when the form is positive definite; the square root exists there, and the first two norm axioms are read off the slot rules of the form, the scaling being $\|\lambda x\| = \lvert\lambda\rvert\|x\|$ with the **modulus** $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$ of the layer in place of the absolute value. **The inequality is an equality for proportional elements.** The Cauchy–Schwarz inequality is proved by translating one argument by a multiple of the other, with $\mu = h(x,y)/h(y,y)$, the translated diagonal being $\|x\|^{2} - \lvert h(x,y)\rvert^{2}/\|y\|^{2}$; the inequality is an equality exactly for proportional elements, and it is the sense in which a definite form is an inner product. **The $\mathrm{C}^*$-condition is a further axiom.** A norm that is already submultiplicative and satisfies $\|x^{*}x\| = \|x\|^{2}$ has an isometric involution, and at $\varsigma = \mathrm{id}$ the condition is the classical $\mathrm{C}^*$-identity; the condition is not automatic, the trace form on $M_{2}(\mathbb{C})$ with the Frobenius norm being submultiplicative and failing the identity at the identity matrix.

The article defines the norm of a definite form and proves the norm axioms, proves the Cauchy–Schwarz inequality and its equality case, derives the triangle inequality and the boundedness of the form, treats the normed and the Banach sesqualgebra with the adjoint pairs and the $\mathrm{C}^*$-condition, and works the examples. Positivity is *Positivity and the Positive Cone of a Hermitian Form*, and the indefinite case, where no norm exists, is *The Indefinite Case and the Signature* and *The Fundamental Symmetry of the Form*. The general inequality for a continuous form that is not definite is *The Cauchy–Schwarz Inequality for Continuous Sesquilinear Maps*, the completion of the normed object *The Completion of a Sesqualgebra with a Form*, the adjoint of an operator *The Adjoint under a Hermitian Form*, the operators and their bounds *Bounded Operators on a Sesqualgebra* and *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*, the normed object without a form *Topological Sesqualgebras*, *Normed and Banach Spaces* and *Banach Sesqualgebras*, the $\mathrm{C}^*$-identity and its consequences *The Involution and the Spectral Radius* and *Involutive Banach Algebras and the Gelfand–Naimark Theorem*, and the passage from an inner product to a Hilbert space and a representation the analysis layer, *Hilbert Spaces* and *Positive Definite Forms and the Order*.

Throughout, the base is of one of the two classical kinds: either $R = k$ is an ordered field with $\varsigma = \mathrm{id}$ in which every nonnegative element is a square, or $R = k(i)$ with $i^{2} = -1$ and $\varsigma$ the conjugation over the ordered field $k$; in the second case every element is uniquely $a + ib$ with $a, b \in k$ and $\lambda\varsigma(\lambda) = a^{2} + b^{2} \geq 0$ with equality only for $\lambda = 0$. In either case $k$ is an ordered field in which every nonnegative element is a square, so the modulus $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$ and the norm below lie in $k$; the model is $R = \mathbb{R}$ with $\varsigma = \mathrm{id}$ and $R = \mathbb{C}$ with the conjugation, $k = \mathbb{R}$. The algebra $A$ is a topological sesqualgebra with a form in the sense of the entry, with continuous Hermitian form $h$ compatible with the product, involution $*$ and derived operation $x \star y = xy^{*}$, and $h$ is positive definite unless a statement says otherwise.

## The Norm of a Definite Form

### The Definite Diagonal

**Definition.** The form $h$ is **positive definite** when $h(x,x) > 0$ for every $x \neq 0$, and **positive semi-definite** when $h(x,x) \geq 0$ for every $x$; the definitions and the four kinds are *Positivity and the Positive Cone of a Hermitian Form*, §*The Four Kinds*. On a positive definite form the **norm** of an element is

$$
\|x\| = h(x,x)^{1/2} ,
$$

the square root being taken in the ordered field $k$ of the nonnegative diagonal.

**Proposition (the diagonal is a fixed scalar and scales by the modulus square).** For every $x$ the value $h(x,x)$ lies in $k = R^{\varsigma}$, and for every $\lambda \in R$,

$$
h(\lambda x, \lambda x) = \lambda\varsigma(\lambda)\,h(x,x) = \lvert\lambda\rvert^{2}\,h(x,x) .
$$

*Proof.* The fixed field is the proposition (the diagonal) of the entry, §*The Definition*, and the scaling is the two slot rules, $h(\lambda x, \lambda x) = \lambda\varsigma(\lambda)h(x,x)$; the second form of the value is the definition of the modulus. $\square$

**Remark.** The scaling by $\lvert\lambda\rvert^{2}$ rather than by $\lambda^{2}$ is the place where the sesquilinear hypothesis enters the homogeneity of the norm, and at $\varsigma = \mathrm{id}$ the modulus of the layer is the absolute value of the ordered field $k$ and the two readings coincide. The fixed field is the natural field of scalars of the norm, since the norm is fixed by the base involution, and it is the field over which the norm's inequalities are read.

### The Norm and Its Axioms

**Theorem (the first two axioms).** Let $h$ be positive definite. Then the map $\|\cdot\| : A \to k$ is nonnegative, it vanishes only at $0$, and it is absolutely homogeneous,

$$
\|x\| \geq 0, \qquad \|x\| = 0 \iff x = 0, \qquad \|\lambda x\| = \lvert\lambda\rvert\,\|x\| .
$$

*Proof.* For the first two, $h(x,x) \geq 0$ with equality exactly for $x = 0$ is the definition of positive definiteness, and the square root is an order isomorphism of the nonnegative elements of $k$ onto themselves. For the third, the scaling proposition gives $\|\lambda x\|^{2} = \lvert\lambda\rvert^{2}\|x\|^{2}$, and both $\|\lambda x\|$ and $\lvert\lambda\rvert\|x\|$ are nonnegative elements of $k$ whose squares agree, so they agree. $\square$

**Remark (the triangle inequality is the third axiom).** It is proved in the next section from the Cauchy–Schwarz inequality, and it is the only axiom that uses the first slot's linearity against the second slot's semilinearity and not merely the diagonal.

### The Definiteness Is the Hypothesis

**Proposition.** A positive semi-definite form that is not definite defines a **seminorm** and no norm: its null set $\{x : h(x,x) = 0\}$ is nonzero, and every element of it has norm zero.

*Proof.* The null set is the set where the norm vanishes, by the definition, and a positive semi-definite form is definite exactly when the null set is zero. $\square$

**Example (a degenerate trace form).** On $M_{2}(\mathbb{C})$ with the conjugate transpose and the form

$$
h(X,Y) = \operatorname{tr}(XE_{11}Y^{*}), \qquad E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},
$$

the diagonal is $h(X,X) = \lvert X_{11}\rvert^{2} + \lvert X_{21}\rvert^{2} \geq 0$, so the form is positive semi-definite, and it is not definite, since the radical of the entry, §*Full Type and Nondegeneracy*, is the nonzero left ideal of the matrices with first column zero. The element $E_{12}$ is nonzero and has norm zero: the norm of the form is a seminorm and not a norm, and after the descent to the quotient by the radical, which is *Positivity and the Positive Cone of a Hermitian Form*, §*The Definite Quotient*, it becomes the norm of the descended definite form.

**Remark.** The hypothesis of definiteness thus enters twice, and both times necessarily: it is what makes the norm vanish only at zero, and it is what makes the translated diagonal of the Cauchy–Schwarz proof vanish only for proportional elements, hence what makes the inequality sharp. An indefinite form has neither property, and its replacement for the norm is the fundamental symmetry of *The Fundamental Symmetry of the Form*.

## The Cauchy–Schwarz Inequality

### The Inequality

**Theorem (Cauchy–Schwarz).** Let $h$ be positive definite. Then

$$
\lvert h(x,y)\rvert^{2} \leq \|x\|^{2}\|y\|^{2} \quad \text{in } k, \qquad \text{equivalently} \qquad \lvert h(x,y)\rvert \leq \|x\|\,\|y\| ,
$$

for all $x, y \in A$, with $\lvert\cdot\rvert$ the modulus of the base.

*Proof.* For $y = 0$ both sides vanish, since $h(x,0) = 0$ by the additivity in the second slot. Let $y \neq 0$, so that $h(y,y) > 0$, and put

$$
\mu = \frac{h(x,y)}{h(y,y)} \in R .
$$

The diagonal of the translated element is expanded by the two slot rules: $h(x - \mu y, x - \mu y) = h(x,x) - \mu\,h(y,x) - \varsigma(\mu)\,h(x,y) + \mu\varsigma(\mu)\,h(y,y)$. Now $h(y,x) = \varsigma(h(x,y))$ by the Hermitian property, and $h(y,y) \in k$ is fixed by $\varsigma$, so that the three terms $\mu\,h(y,x)$, $\varsigma(\mu)\,h(x,y)$ and $\mu\varsigma(\mu)\,h(y,y)$ all equal $h(x,y)\varsigma(h(x,y))/h(y,y)$, the first two entering with the sign $-$ and the third with the sign $+$; the three sum to $-h(x,y)\varsigma(h(x,y))/h(y,y)$, so that the translated diagonal is

$$
h(x - \mu y, x - \mu y) = h(x,x) - \frac{h(x,y)\,\varsigma(h(x,y))}{h(y,y)} = \|x\|^{2} - \frac{\lvert h(x,y)\rvert^{2}}{\|y\|^{2}} .
$$

The form is positive definite, so the left side is $\geq 0$, and multiplying the inequality by $\|y\|^{2} > 0$ in the ordered field $k$ gives the claim. $\square$

**Remark (the shape of the proof).** The proof is the two-variable form of the discriminant argument for a quadratic form of one variable: the diagonal of the translated element is a nonnegative quadratic in $\mu$ with the leading coefficient $\|y\|^{2}$, and the inequality says that its discriminant is $\leq 0$. The discriminant argument is available because the leading coefficient is a fixed positive scalar, that is because the diagonal lies in $k$; on a general sesqualgebra over a general involutive ring the argument is replaced by the continuous version of *The Cauchy–Schwarz Inequality for Continuous Sesquilinear Maps*, and here the definite case is the sharp one.

### The Equality Case

**Theorem.** Let $h$ be positive definite. Then the Cauchy–Schwarz inequality is an equality exactly when $x$ and $y$ are linearly dependent.

*Proof.* If $y \neq 0$ the proof above shows that the equality holds exactly when $h(x - \mu y, x - \mu y) = 0$, which by definiteness is $x = \mu y$. If $y = 0$ both sides vanish and $x, y$ are dependent. Conversely, if $x = \mu y$ then $h(x,y) = \mu h(y,y)$ with $h(y,y) \in k$, so $\lvert h(x,y)\rvert = \lvert\mu\rvert h(y,y)$ and $\|x\| = \lvert\mu\rvert\|y\|$, and the product of the two is $\lvert h(x,y)\rvert$. $\square$

**Corollary (the definite form is an inner product).** The inequality says that the Hermitian form is an inner product in the norm it defines: it is definite, Hermitian and bounded with constant one, so it is a definite Hermitian pairing of the normed module with itself, and the equality case of the inequality is the degenerate case of two proportional vectors, which is the classical form of the equality of an inner product. The passage from that inner product to the Hilbert space and to the representation of the algebra is *Positive Definite Forms and the Order* and *Hilbert Spaces*.

### The Boundedness of the Form

**Corollary (the form is continuous).** Let $h$ be positive definite. Then $\lvert h(x,y)\rvert \leq \|x\|\|y\|$, so $h$ is continuous for the norm topology, with the operator norm at most one; consequently the form of the layer is automatically continuous when it is definite and the topology is that of its norm.

*Proof.* The inequality is Cauchy–Schwarz, and it says that $h$ maps the product of the unit balls into the set of elements of modulus at most one, which is bounded; bilinearity then gives continuity. $\square$

**Remark.** The corollary is the reason the continuity that the layer imposes on its forms is not an extra hypothesis in the definite case: the norm of the form supplies it. It also shows that the form is a bounded pairing of the normed module with itself, which is the hypothesis under which the adjoint of an operator is defined in *The Adjoint under a Hermitian Form* and in *Bounded Operators on a Sesqualgebra*.

### The Triangle Inequality

**Lemma (the real part is at most the modulus).** For every $t \in R$ the inequality $t + \varsigma(t) \leq 2\lvert t\rvert$ holds in $k$.

*Proof.* In the base $k(i)$ write $t = a + ib$ with $a, b \in k$; then $t + \varsigma(t) = 2a$ and $\lvert t\rvert = (a^{2} + b^{2})^{1/2} \geq \lvert a\rvert \geq a$, since $b^{2} \geq 0$. In the base $k$ with $\varsigma = \mathrm{id}$ the inequality is $2t \leq 2\lvert t\rvert$, which is the definition of the absolute value of the ordered field. $\square$

**Theorem (the triangle inequality).** Let $h$ be positive definite. Then

$$
\|x + y\| \leq \|x\| + \|y\| .
$$

*Proof.* Expanding the diagonal of a sum by the two slot rules,

$$
\|x+y\|^{2} = h(x,x) + h(x,y) + h(y,x) + h(y,y) = \|x\|^{2} + \bigl(h(x,y) + \varsigma(h(x,y))\bigr) + \|y\|^{2} ,
$$

the middle term is in $k$ because it is fixed by $\varsigma$, and the lemma bounds it by $2\lvert h(x,y)\rvert$, which Cauchy–Schwarz bounds by $2\|x\|\|y\|$. Hence $\|x+y\|^{2} \leq (\|x\| + \|y\|)^{2}$, and both sides are nonnegative elements of the ordered field $k$, so the square roots are ordered as claimed. $\square$

**Corollary (the norm of the form).** The three axioms together say that $\|\cdot\|$ is a norm on the module $A$: it is nonnegative and definite, absolutely homogeneous with the modulus of the base as the absolute value, and subadditive. The pair $(A,\|\cdot\|)$ is therefore a normed $R$-module in the sense of *Normed and Banach Spaces*, and its norm is determined by the diagonal of the form alone.

## The Normed and the Banach Sesqualgebra

### The Submultiplicative Norm

**Definition.** A topological sesqualgebra with a form is **normed by its form** when the form is positive definite, the topology is that of its norm, and the norm is **submultiplicative**,

$$
\|xy\| \leq \|x\|\,\|y\| \qquad \text{for all } x, y \in A .
$$

It is a **Banach sesqualgebra with a form** when in addition the normed module is complete.

**Remark (submultiplicativity is an axiom).** The inequality is not a consequence of the definiteness, and it is the one condition that ties the norm of the form to the product; it is the analogue for a form of the submultiplicativity that defines a normed algebra, and a form norm that satisfies it is an algebra norm. The object without the form, whose norm is submultiplicative by definition, is *Banach Sesqualgebras* and *Topological Algebras and Banach Algebras*; the completion of the normed object here is *The Completion of a Sesqualgebra with a Form*.

### The Adjoint Pairs and the Operator Norm

**Theorem (the multiplications are bounded and adjoint).** Let the object be normed by its form. Then for every $x$ the left multiplications $m_{x} : z \mapsto xz$ and $m_{x^{*}} : z \mapsto x^{*}z$ are bounded operators of norm at most $\|x\|$ and $\|x^{*}\|$, and they are adjoint to one another for $h$:

$$
h(m_{x}z, w) = h(z, m_{x^{*}}w) \qquad \text{for all } z, w \in A .
$$

*Proof.* The bound $\|m_{x}z\| = \|xz\| \leq \|x\|\|z\|$ is submultiplicativity, which gives the boundedness and the estimate on the operator norm; the adjointness is the compatibility $h(xz,w) = h(z,x^{*}w)$ of the entry, §*The Compatibility*. $\square$

**Remark (the two norms need not agree).** The operator norm of $m_{x}$ is at most $\|x\|$, and the two need not be equal: on $M_{2}(\mathbb{C})$ with the trace form the norm is the Frobenius norm of the example below, and for the identity matrix $m_{1}$ is the identity operator, of operator norm $1$, while $\|1\| = \sqrt{2}$. The agreement of the two norms is the statement that the left regular representation is isometric, and it is a further condition on the object, treated for the multiplications by *The Bounded Left and Right Multiplication Operators of a Sesqualgebra*.

### The $\mathrm{C}^*$-Condition

**Definition.** Say that the norm of the form satisfies the **$\mathrm{C}^*$-condition** when

$$
\|x^{*}x\| = \|x\|^{2} \qquad \text{for every } x \in A ,
$$

where $x^{*}x$ is the Hermitian element $\Psi(x,x)$ of *Hermitian Forms on a Sesqualgebra*, §*The Diagonal*, that is, the diagonal value at $(x,x)$ of the $A$-valued form $\Psi$ of the involution.

**Theorem (the involution is isometric).** Let the object be normed by its form and let the $\mathrm{C}^*$-condition hold. Then

$$
\|x^{*}\| = \|x\| \qquad \text{for every } x \in A ,
$$

so the involution is an isometry of the normed module and is continuous.

*Proof.* The $\mathrm{C}^*$-condition and submultiplicativity give $\|x\|^{2} = \|x^{*}x\| \leq \|x^{*}\|\|x\|$, hence $\|x\| \leq \|x^{*}\|$ when $x \neq 0$ and trivially otherwise; the same argument with $x^{*}$ in place of $x$ gives $\|x^{*}\| \leq \|x\|$, because $(x^{*})^{*} = x$. $\square$

**Theorem (the diagonal computes the norm).** Under the same hypotheses the norm is determined by the Hermitian squares,

$$
\|x\|^{2} = \|x^{*}x\| ,
$$

and the scalar reading of the same element is the diagonal of the form, $h(x,x) = \varphi(x^{*}x)$ for the functional $\varphi$ of *The Sesquilinear Form and the Conjugation*, §*The Reconstruction*, so that the form's diagonal, the Hermitian square and the norm are three readings of one datum.

*Proof.* The first identity is the condition, and the second is the reconstruction of the form from its functional at the pair $(x,x)$. $\square$

**Remark (the condition is a restriction).** The $\mathrm{C}^*$-condition is not automatic and not implied by submultiplicativity: on $M_{n}(\mathbb{C})$ with the trace form the norm is the Frobenius norm of the examples below, which is submultiplicative, and at the identity matrix

$$
\|1\|^{2} = n, \qquad \|1^{*}1\| = \|1\| = \sqrt{n} ,
$$

so the condition fails for $n \geq 2$; the equality holds at $1$ exactly when $n = 1$. The condition holds for the norm of the field example and, in general, it is the hypothesis under which the norm of the form is an algebra norm compatible with the involution, its classical instance being the $\mathrm{C}^*$-identity of *The Involution and the Spectral Radius* and *Involutive Banach Algebras and the Gelfand–Naimark Theorem*.

## The Collapse at the Trivial Involution

### The Bilinear Reading

**Theorem (the collapse).** Let $\varsigma = \mathrm{id}$, so that $R = k$ and the form is symmetric and $k$-bilinear. Then the norm of the form is the norm of the symmetric positive definite form, $\|x\| = h(x,x)^{1/2}$, the scaling reads $\|\lambda x\| = \lvert\lambda\rvert\|x\|$ with the absolute value of the ordered field, the compatibility is the invariance $h(xy,z) = h(y,xz)$ whose left multiplications are self-adjoint, and the $\mathrm{C}^*$-condition is the classical $\mathrm{C}^*$-identity $\|x^{*}x\| = \|x\|^{2}$ of an involutive normed algebra.

*Proof.* Each statement is the corresponding statement above read at $\varsigma = \mathrm{id}$: the modulus is the absolute value, the form of the layer is bilinear by the collapse of *Topological Sesqualgebras with a Form*, §*The Collapse at the Trivial Involution*, and the identity is the one of the cited article on the $\mathrm{C}^*$-identity. $\square$

**Remark (which statements are sesquilinear).** The norm axioms and the inequality are the same in the two categories and are therefore not sesquilinear statements; the sesquilinear content of the article lies in the scaling $\|\lambda x\| = \lvert\lambda\rvert\|x\|$ with $\lvert\lambda\rvert^{2} = \lambda\varsigma(\lambda)$ rather than $\lambda^{2}$, and in the fact that the norm is read from the diagonal of a form that is Hermitian and not symmetric. At the collapse the object is a normed involutive algebra with a symmetric definite form, whose completed theory is *Involutive Banach Algebras and the Gelfand–Naimark Theorem*, and the bilinear model of the whole article is the Hilbert algebra of *Hilbert Algebras*, where the same form axiom is read with $\varsigma = \mathrm{id}$.

## Examples

### The Field

**Example (the complex field).** Let $R = k(i) = \mathbb{C}$, let $A = \mathbb{C}$ with the algebra product, $* = \varsigma$ the conjugation and $h(z,w) = z\varsigma(w) = z\overline{w}$, the form of *Topological Sesqualgebras with a Form*, §*The Examples of the Layer*. The form is Hermitian, compatible and positive definite, and the norm is $\|z\| = (z\overline{z})^{1/2} = \lvert z\rvert$, the modulus of the field: the norm of the form is the Euclidean norm of the plane, the Cauchy–Schwarz inequality is the identity $\lvert z\overline{w}\rvert = \lvert z\rvert\lvert w\rvert$, an equality for every pair because the two elements of a one-dimensional space are always proportional. The example is the collapsed case read at the level of the norm as well: with $k$ in place of $\mathbb{C}$ the same computation is the norm of the field and *Quadratic Forms over Algebras and Norms* records the norm of $\mathbb{C}$ among those of the number systems.

### The Matrix Algebra

**Example (the Frobenius norm).** Let $A = M_{n}(\mathbb{C})$ with the conjugate transpose and the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$, the model of the layer. The norm is

$$
\|X\| = \operatorname{tr}(XX^{*})^{1/2} = \Bigl(\sum_{i,j}\lvert X_{ij}\rvert^{2}\Bigr)^{1/2} ,
$$

the **Frobenius norm**, which is the Euclidean norm of the $n^{2}$ entries: it is submultiplicative, and the Gram matrix of the form in the basis of the matrix units is the identity, so the form is nondegenerate with $\|E_{ij}\| = 1$ on the units. Cauchy–Schwarz is the inequality $\lvert\operatorname{tr}(XY^{*})\rvert \leq \|X\|\|Y\|$, the equality case being proportionality, and the form is bounded with constant one. The norm is not the $\mathrm{C}^*$-norm: $\|1\|^{2} = n$ while $\|1^{*}1\| = \sqrt{n}$, so the $\mathrm{C}^*$-condition fails for $n \geq 2$, and for $n = 2$ the operator norm of $m_{1}$ is $1$ while $\|1\| = \sqrt{2}$. The example is the model of the article and the witness that the $\mathrm{C}^*$-condition is a restriction on the object and not a consequence of the definiteness.

### The Biquaternion Trace Form

**Example (the biquaternion algebra).** On the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the Hermitian conjugation $* = {}^{\natural} \circ \bar{\cdot}$ the **complex sesquilinear** form of *The Four Pairings of the Biquaternion Algebra*, §*The Four Pairings*,

$$
h(P,Q) = \operatorname{Sc}(PQ^{*}) = \sum_{\mu} P_{\mu}\,\varsigma(Q_{\mu}),
$$

is Hermitian, compatible, nondegenerate and positive definite, of signature $(8,0)$ over $\mathbb{R}$, and the norm it defines is the Euclidean norm of the eight real coordinates, the one of *The Euclidean Topology of the Biquaternion Algebra*: $\|Q\| = \operatorname{Sc}(QQ^{*})^{1/2} = (\sum_\mu \lvert Q_\mu\rvert^{2})^{1/2}$. The diagonal is the sum of the four squared moduli of the coefficients, and the compatibility is the adjoint rule $(L_{Q})^{\langle\cdot,\cdot\rangle_{*}} = L_{Q^{*}}$ of *The Four Pairings of the Biquaternion Algebra*, §*The Forms in Comparison*; the other three pairings of that article — the two bilinear ones, of signature $(4,4)$, and the quaternion sesquilinear one, of signature $(2,6)$ — are not positive definite and define no norm of this article, and the last of them is not even compatible with the product. The example is the finite-dimensional instance in which the four pairings of the biquaternion algebra are compared, and the definite one among them is the norm.

### The Collapsed Field

**Example (the collapsed field).** Let $R = k$ be an ordered field with $\varsigma = \mathrm{id}$, let $A = k$ with the algebra product and $h(x,y) = xy$. The form is symmetric, bilinear and positive definite, the norm is $\|x\| = \lvert x\rvert$ and the series of statements of the article is the classical one of the ordered field: the collapse of the section above, with the sesquilinear reading of the scaling reduced to the absolute value.

## Summary

A **positive definite** Hermitian form is a **norm**: on the diagonal, $h(x,x) \in k = R^{\varsigma}$ and $h(x,x) > 0$ for $x \neq 0$, so the square root $\|x\| = h(x,x)^{1/2}$ lies in the ordered field of scalars, and the norm axioms hold — nondegeneracy and positivity from the definiteness, absolute homogeneity $\|\lambda x\| = \lvert\lambda\rvert\|x\|$ from the slot rules with the modulus $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$, and the triangle inequality from the Cauchy–Schwarz inequality. The **Cauchy–Schwarz inequality** $\lvert h(x,y)\rvert^{2} \leq \|x\|^{2}\|y\|^{2}$ is proved by the translated diagonal $h(x - \mu y, x - \mu y) = \|x\|^{2} - \lvert h(x,y)\rvert^{2}/\|y\|^{2}$ with $\mu = h(x,y)/h(y,y)$, and it is an equality exactly for linearly dependent elements; it makes the form a bounded pairing, continuous with constant one, and with the lemma $h(x,y) + \varsigma(h(x,y)) \leq 2\lvert h(x,y)\rvert$ it gives the **triangle inequality** $\|x+y\| \leq \|x\| + \|y\|$. The definite form is therefore an inner product on a normed module, and the two facts that the norm is submultiplicative and that it satisfies the **$\mathrm{C}^*$-condition** $\|x^{*}x\| = \|x\|^{2}$ are the axioms that make the object a **normed**, and when complete a **Banach**, sesqualgebra with a form: the first ties the norm to the product, the second ties it to the involution, and together they give the isometric involution $\|x^{*}\| = \|x\|$. Neither is automatic: the trace form on $M_{n}(\mathbb{C})$ has the submultiplicative Frobenius norm for which $\|1\|^{2} = n$ and $\|1^{*}1\| = \sqrt{n}$ differ for $n \geq 2$, and a semi-definite form that is not definite defines a seminorm whose null set is the radical, such as $\operatorname{tr}(XE_{11}Y^{*})$ on $M_{n}(\mathbb{C})$. At $\varsigma = \mathrm{id}$ the modulus is the absolute value, the form is symmetric and bilinear, the left multiplications are self-adjoint, and the $\mathrm{C}^*$-condition is the classical $\mathrm{C}^*$-identity: the article collapses to the normed involutive algebra of the bilinear layer, whose model is the Hilbert algebra. The examples are the complex field with the modulus, the matrix algebra with the Frobenius norm, the biquaternion algebra with its complex sesquilinear form and the Euclidean norm, and the collapsed field.

## Summary of Notation

| symbol | meaning |
|---|---|
| $h(x,x)$ | the diagonal, in $k = R^{\varsigma}$; $> 0$ for $x \neq 0$ exactly when the form is positive definite |
| $\|x\| = h(x,x)^{1/2}$ | the norm defined by a positive definite form, with values in the ordered field $k$ |
| $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$ | the modulus of the base, in $k$; the absolute value at $\varsigma = \mathrm{id}$ |
| $\|\lambda x\| = \lvert\lambda\rvert\|x\|$ | absolute homogeneity, the sesquilinear reading of the scaling |
| $\lvert h(x,y)\rvert^{2} \leq \|x\|^{2}\|y\|^{2}$ | the Cauchy–Schwarz inequality, an equality exactly for dependent elements |
| $h(x-\mu y, x-\mu y) = \|x\|^{2} - \lvert h(x,y)\rvert^{2}/\|y\|^{2}$ | the translated diagonal, $\mu = h(x,y)/h(y,y)$, with which the inequality is proved |
| $\lvert h(x,y)\rvert \leq \|x\|\|y\|$ | the boundedness of the form, hence its continuity for the norm topology |
| $\|x+y\| \leq \|x\| + \|y\|$ | the triangle inequality, from the inequality and $t + \varsigma(t) \leq 2\lvert t\rvert$ |
| $\|xy\| \leq \|x\|\|y\|$ | submultiplicativity, the axiom that makes the norm an algebra norm |
| $h(xz,w) = h(z,x^{*}w)$ | the adjoint pair $m_{x}$, $m_{x^{*}}$, with operator norm at most $\|x\|$, $\|x^{*}\|$ |
| $\|x^{*}x\| = \|x\|^{2}$ | the $\mathrm{C}^*$-condition, which gives the isometric involution $\|x^{*}\| = \|x\|$ |
| $\operatorname{tr}(XX^{*})^{1/2}$ | the Frobenius norm on $M_{n}(\mathbb{C})$, submultiplicative and not a $\mathrm{C}^*$-norm for $n \geq 2$ |
| $\varsigma = \mathrm{id}$ | the collapse: symmetric bilinear form, self-adjoint left multiplications, classical $\mathrm{C}^*$-identity |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the Cauchy–Schwarz inequality, the triangle inequality and the passage from an inner product to a norm.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the $\mathrm{C}^*$-identity and its consequences for the norm.
- Gerard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for the $\mathrm{C}^*$-condition, submultiplicativity and isometric involutions.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the positive involution of the base and the modulus of a field with involution.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the definite Hermitian forms over a field with an involution and their Gram matrices.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the Frobenius norm, its submultiplicativity and the failure of the $\mathrm{C}^*$-identity for it.
