# __The Cauchy–Schwarz Inequality for Continuous Sesquilinear Maps__

## Introduction

The Cauchy–Schwarz inequality of the definite theory, $\lvert h(x,y)\rvert^{2} \leq \lVert x\rVert^{2}\lVert y\rVert^{2}$, is proved in *The Norm Defined by a Form* by dividing by $h(y,y)$ and using that the translated diagonal is nonnegative. Definiteness enters twice there: it makes $h(y,y) > 0$ for $y \neq 0$, and it makes the translated diagonal vanish only at proportional elements, hence the inequality sharp. Neither use is necessary for the inequality itself. **Positivity alone suffices**: if $h$ is Hermitian with $h(x,x) \geq 0$ for every $x$, then

$$
\varsigma(h(x,y))\,h(x,y) \leq h(x,x)\,h(y,y) \quad \text{in } R^{\varsigma},
$$

and the degenerate case $h(y,y) = 0$ is not an exception but the case in which the translated quadratic in a real parameter forces $h(x,y) = 0$. This article proves that inequality for a **sesquilinear map** whose values may lie in the base $R$ or in an algebra $A$ or a $\mathrm{C}^{*}$-algebra $B$, and reads from it the seminorm that the positive semi-definite form defines, the reduction of continuity to a single scalar function, and the equality case.

Three facts organise the article. **The inequality is proved by translating one argument.** With $\mu = h(x,y)/h(y,y)$ the diagonal of $x - \mu y$ is $h(x,x) - \lvert h(x,y)\rvert^{2}/h(y,y)$, and its nonnegativity is the inequality; the proof of the definite case is the same computation and the difference is only that the division by $h(y,y)$ is now allowed exactly when $h(y,y) \neq 0$, the degenerate case being settled by a real-parameter argument that forces $h(x,y) = 0$ before the division is attempted. **The diagonal is a seminorm, and the positive maps are determined by it.** The function $p(x) = h(x,x)^{1/2}$ is a seminorm on the module, its triangle inequality being the inequality itself; the null set $\{x : h(x,x) = 0\}$ is the radical of the form, so $p$ is a norm exactly on the definite quotient and the completion is a Hilbert space; and for a positive map the whole continuity is the boundedness of $p^{2}$ on the unit ball, $\lVert h\rVert = \sup_{\lVert x\rVert \leq 1}h(x,x)$, so the passage from positivity to continuity is the boundedness of one scalar function. **That boundedness is not free.** Positivity does not bound the diagonal on a non-complete module, the rank-one map of an unbounded functional being the witness, and the article records the hypothesis rather than claiming the automatic continuity that the layer does not have; on the objects of the layer the form is continuous by hypothesis, and in the definite case the norm of the form supplies the bound with constant one.

The article defines the positive sesquilinear maps and their two kinds of values, proves the Cauchy–Schwarz inequality, its degenerate case and its equality case, reads the seminorm, the radical and the definite quotient, proves the reduction of continuity to the diagonal and gives the witness that positivity alone does not bound it, treats the $\mathrm{C}^{*}$-valued maps and the norm inequality that reduces to the scalar case, records the collapse at the trivial involution, and works the examples. The definite case, its norm and its sharp constant are *The Norm Defined by a Form*; the four kinds of form and the identification of the null set with the radical are *Positivity and the Positive Cone of a Hermitian Form*; the failure of the inequality for an indefinite form is *The Indefinite Case and the Signature*; the functional pairing $s(x,y) = f(y^{*}x)$ of a positive functional, its inequality and the continuity of positive functionals are *States and Positive Functionals on a Topological Sesqualgebra*; the universal $A$-valued form $\Psi(x,y) = y^{*}x$, the module inequality and its sharp algebraic form are *Hermitian Forms on a Sesqualgebra*, *Adjoints of Bounded Sesquilinear Operators* and *Hilbert and $\mathrm{C}^{*}$-Modules*; the sesquilinear form of the layer, the radical and the compatibility are *Topological Sesqualgebras with a Form*; the complete objects are *Banach Sesqualgebras*; and the completion of an inner product space is *Hilbert Spaces*.

**Conventions.** The base is $(R,\varsigma)$ with $R$ a field, $\varsigma$ an involution of it and $k = R^{\varsigma}$ an ordered field in which every nonnegative element is a square, the model being $R = \mathbb{R}$ with $\varsigma = \mathrm{id}$ and $R = \mathbb{C}$ with the conjugation; the **modulus** of a scalar is $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2} \in k$. A **sesquilinear map** is a biadditive $s : A \times A \to B$ with

$$
s(\lambda x,y) = \lambda\,s(x,y), \qquad s(x,\lambda y) = \varsigma(\lambda)\,s(x,y),
$$

$R$-linear in the first slot and $\varsigma$-semilinear in the second, the convention of *Topological Sesqualgebras with a Form*, §*The Definition*; it is **Hermitian** when $s(y,x) = \varsigma(s(x,y))$ for $B = R$ and $s(y,x) = s(x,y)^{*}$ for $B$ an algebra with involution, and **positive** when $s(x,x) \geq 0$ for every $x$, in the orders of $k$ and of $B$ respectively. The values are either in the base $R$ — a **sesquilinear form** — or in $A$ itself or in a $\mathrm{C}^{*}$-algebra $B$ — the **sesquilinear maps** of the operator layers. The module carries a norm $\lVert\cdot\rVert$, the bound of $s$ is $\lVert s\rVert = \sup\{\lVert s(x,y)\rVert : \lVert x\rVert \leq 1, \lVert y\rVert \leq 1\}$, and $s$ is continuous exactly when the bound is finite.

## The Positive Sesquilinear Maps

### The Two Kinds of Value

**Definition.** A sesquilinear map $s$ with values in $R$ is a **form**; with values in an involutive $R$-algebra $B$ it is an **algebra-valued map**. In both cases $s$ is **Hermitian** when the exchange of the arguments conjugates the value, and **positive** when the diagonal is nonnegative, $s(x,x) \geq 0$ in $k$ in the first case and $s(x,x) \geq 0$ in $B$ in the second. The form is **positive definite** when $s(x,x) > 0$ for $x \neq 0$ and **positive semi-definite** when $s(x,x) \geq 0$; the four kinds and their signs are *Positivity and the Positive Cone of a Hermitian Form*, §*The Four Kinds*.

**Proposition (the diagonal is a fixed scalar).** Let $s$ be Hermitian with values in $R$. Then $s(x,x) = \varsigma(s(x,x))$ for every $x$, so the diagonal takes its values in the fixed field $k$; and for $\lambda \in R$ the diagonal scales as

$$
s(\lambda x,\lambda x) = \lambda\varsigma(\lambda)\,s(x,x) = \lvert\lambda\rvert^{2}s(x,x) .
$$

*Proof.* The first is the Hermitian property at the pair $(x,x)$; the second is the two slot rules applied in sequence, $s(\lambda x,\lambda y) = \lambda\varsigma(\lambda)s(x,y)$. $\square$

**Remark (the model).** The canonical example of the article is the pairing of a positive functional, $s(x,y) = f(y^{*}x)$, whose values lie in $\mathbb{C}$, and the canonical example with values in $A$ is $\Psi(x,y) = y^{*}x$ itself, the universal $A$-valued form of *Hermitian Forms on a Sesqualgebra*, §*The Reduction to the Scalars*; the two are related by the reduction of the second along $f$, and the scalar theory of the article is the common part of the two. The scalar reductions $\varphi \circ s$ of a $B$-valued map along the functionals of $B$ are the device by which the algebra-valued statements below are reduced to the scalar ones.

### Positivity

**Proposition (the scalar reductions of a positive map are positive).** Let $s : A \times A \to B$ be a sesquilinear map with values in a $\mathrm{C}^{*}$-algebra $B$. Then $s$ is positive iff every positive functional $\varphi$ of $B$ has $\varphi \circ s$ positive; and a positive map is Hermitian automatically, since its scalar reductions are Hermitian forms and the states separate $B$.

*Proof.* If $s$ is positive then $\varphi(s(x,x)) \geq 0$ for every positive functional $\varphi$, so $\varphi \circ s$ is positive; conversely $s(x,x) \geq 0$ in $B$ iff $\varphi(s(x,x)) \geq 0$ for every state $\varphi$ of $B$, by the representation of the order of a $\mathrm{C}^{*}$-algebra through its states. For the Hermitian clause, let $s$ be positive and let $\varphi$ be a state; the scalar form $\varphi \circ s$ is positive, and a scalar-valued positive sesquilinear form is Hermitian, so $\varphi(s(x,y)) = \varsigma(\varphi(s(y,x))) = \varphi(s(y,x)^{*})$ for every state $\varphi$; the states separate the elements of $B$, whence $s(x,y) = s(y,x)^{*}$, the Hermitian property. $\square$

## The Inequality

### The Statement

**Theorem (Cauchy–Schwarz).** Let $s$ be Hermitian and positive semi-definite with values in $R$. Then for all $x, y \in A$,

$$
\varsigma(s(x,y))\,s(x,y) \leq s(x,x)\,s(y,y) \quad \text{in } k, \qquad \text{equivalently} \qquad \lvert s(x,y)\rvert^{2} \leq s(x,x)\,s(y,y) ,
$$

with $\lvert\cdot\rvert$ the modulus of the base. Definiteness is not assumed, and when $s(y,y) = 0$ the inequality reads $s(x,y) = 0$.

*Proof.* For $y = 0$ both sides vanish. Let $s(y,y) \neq 0$. It lies in $k$ and is positive, so it is invertible in $k$ and $\mu = s(x,y)/s(y,y) \in R$. Expand the diagonal of $x - \mu y$ by the two slot rules:

$$
s(x-\mu y,x-\mu y) = s(x,x) - \mu\,s(y,x) - \varsigma(\mu)\,s(x,y) + \mu\varsigma(\mu)\,s(y,y) .
$$

By the Hermitian property $s(y,x) = \varsigma(s(x,y))$, and $s(y,y) \in k$ is fixed by $\varsigma$, so the three terms $\mu\,s(y,x)$, $\varsigma(\mu)\,s(x,y)$ and $\mu\varsigma(\mu)\,s(y,y)$ each equal $s(x,y)\varsigma(s(x,y))/s(y,y) = \lvert s(x,y)\rvert^{2}/s(y,y)$, the first two with the sign $-$ and the third with the sign $+$; the translated diagonal is therefore

$$
s(x-\mu y,x-\mu y) = s(x,x) - \frac{\lvert s(x,y)\rvert^{2}}{s(y,y)} .
$$

The form is positive, so the left side is $\geq 0$, and multiplying the inequality by $s(y,y) > 0$ in the ordered field $k$ gives the claim. $\square$

### The Degenerate Case

**Proposition (the neutral argument).** Let $s$ be Hermitian and positive semi-definite and let $s(y,y) = 0$. Then $s(x,y) = 0$ for every $x$, and consequently $y$ lies in the radical of $s$ and the inequality holds with both sides zero.

*Proof.* For $\lambda \in k$, which is fixed by $\varsigma$, the diagonal of $x - \lambda y$ is $s(x,x) - \lambda s(y,x) - \lambda s(x,y) = s(x,x) - 2\lambda\,\mathrm{Re}\,s(x,y)$, where $\mathrm{Re}\,t = \tfrac12(t + \varsigma(t))$ is the fixed part; the form is positive, so $s(x,x) \geq 2\lambda\,\mathrm{Re}\,s(x,y)$ for every $\lambda \in k$, which forces $\mathrm{Re}\,s(x,y) = 0$. In the bilinear kind $s$ is already fixed and $s(x,y) = 0$; in the sesquilinear kind apply the same argument at the pair $(ix,y)$, whose fixed part is $\mathrm{Re}\,s(ix,y) = \mathrm{Re}(i\,s(x,y)) = -\mathrm{Im}\,s(x,y)$, and get $\mathrm{Im}\,s(x,y) = 0$ as well. Hence $s(x,y) = 0$ for every $x$, so $y$ is in the radical, $\mathrm{rad}(s) = \{x : s(x,y) = 0 \text{ for all } y\}$; and the inequality reads $0 \leq s(x,x)\cdot 0$. $\square$

**Remark (the proof is the same as the definite one).** The definite proof of *The Norm Defined by a Form*, §*The Inequality*, is the computation above with the division available; the degenerate case is not a pathology of the inequality but the case in which the translated diagonal has the leading coefficient $s(y,y) = 0$ and the quadratic in the real parameter forces the vanishing of the value instead of bounding its square. The indefinite case lies in the other direction and is excluded: for an indefinite form $s(y,y)$ may be negative, the translation by $\mu$ is not available and the inequality fails, with the neutral pair $e_{1} + e_{2}$, $e_{1} - e_{2}$ of the hyperbolic plane as the witness of *The Indefinite Case and the Signature*, §*The Cauchy–Schwarz Inequality Fails*.

### The Equality Case

**Theorem (the equality case).** Let $s$ be Hermitian and positive semi-definite with values in $R$. Then the inequality is an equality exactly for the pairs that are linearly dependent modulo the radical: $\lvert s(x,y)\rvert^{2} = s(x,x)s(y,y)$ iff there is $\mu \in R$ with $x - \mu y \in \mathrm{rad}(s)$, or $y \in \mathrm{rad}(s)$.

*Proof.* If $s(y,y) = 0$ then $s(y,x) = 0$ for every $x$ and $y \in \mathrm{rad}(s)$, and both sides of the inequality vanish for every $x$, so the equality holds on the whole class of $y$ modulo the radical and the statement is the case $y \in \mathrm{rad}(s)$. Let $s(y,y) > 0$ and put $\mu = s(x,y)/s(y,y)$. The proof of the inequality shows that the equality holds exactly when $s(x-\mu y,x-\mu y) = 0$; by the proposition above the null set of a positive semi-definite form is its radical, so this is $x - \mu y \in \mathrm{rad}(s)$. Conversely if $x = \mu y + z$ with $z \in \mathrm{rad}(s)$ then $s(x,x) = \lvert\mu\rvert^{2}s(y,y)$ and $s(x,y) = \mu\,s(y,y)$, so $\lvert s(x,y)\rvert^{2} = \lvert\mu\rvert^{2}s(y,y)^{2} = s(x,x)s(y,y)$. $\square$

**Corollary (the definite case is the sharp one).** When $s$ is positive definite its radical is zero and the equality case is the proportionality of *The Norm Defined by a Form*, §*The Equality Case*: the inequality is an equality exactly for linearly dependent elements. The general statement is the same statement read modulo the radical, and the definite case is the case in which the radical has been divided out.

## The Seminorm, the Radical and the Quotient

### The Seminorm

**Theorem (the diagonal is a seminorm).** Let $s$ be Hermitian and positive semi-definite with values in $R$. Then $p(x) = s(x,x)^{1/2}$ is a seminorm on $A$,

$$
p(x) \geq 0, \qquad p(\lambda x) = \lvert\lambda\rvert\,p(x), \qquad p(x+y) \leq p(x) + p(y),
$$

and $\lvert s(x,y)\rvert \leq p(x)p(y)$; the null set $\{x : p(x) = 0\} = \{x : s(x,x) = 0\}$ is the radical of $s$.

*Proof.* The first two are the proposition on the diagonal and the square root in $k$. For the third, the expansion of the diagonal of a sum gives $s(x+y,x+y) = s(x,x) + s(x,y) + \varsigma(s(x,y)) + s(y,y) = p(x)^{2} + 2\,\mathrm{Re}\,s(x,y) + p(y)^{2} \leq p(x)^{2} + 2p(x)p(y) + p(y)^{2}$, using $\mathrm{Re}\,t \leq \lvert t\rvert$ and the inequality; the square roots in $k$ are ordered, so $p(x+y) \leq p(x)+p(y)$. The inequality for $\lvert s(x,y)\rvert$ is Cauchy–Schwarz. The null set is the radical by the proposition of the degenerate case, which shows both inclusions. $\square$

**Remark (the null set is the radical, and the norm is the definite case).** The identity $\{s(x,x) = 0\} = \mathrm{rad}(s)$ for a positive semi-definite form is the statement that *Positivity and the Positive Cone of a Hermitian Form*, §*The Null Set and the Radical*, proves from the inequality and its equality case and that this article supplies; the seminorm is a norm exactly when the form is definite, which is the case of *The Norm Defined by a Form*.

### The Definite Quotient and the Completion

**Theorem (the quotient).** Let $s$ be Hermitian and positive semi-definite with radical $N = \mathrm{rad}(s)$, a subspace of $A$ on which $s$ vanishes in both arguments. Then $s$ descends to the quotient $A/N$ as a positive definite Hermitian form

$$
\bar{s}(x + N, y + N) = s(x,y),
$$

which is well defined, and the seminorm $p$ descends to the norm $\lVert x + N\rVert = p(x)$ of the completed inner product space.

*Proof.* The form vanishes on $N$ in both arguments, so the value depends only on the classes; it is Hermitian and positive because $s$ is, and it is definite because a class with $\bar{s}(\xi,\xi) = 0$ is represented by an element of the null set, that is of $N$. The completion of the resulting inner product space is a Hilbert space, *Hilbert Spaces*, §*Completeness and the Projection Theorem*, and the seminorm descends to the norm of the quotient. $\square$

**Remark (the construction is the GNS construction).** The quotient, the completion and the representation that the completed inner product carries are the construction of *States and Positive Functionals on a Topological Sesqualgebra*, §*The GNS Construction*, in the case in which the map is the pairing of a functional; the abstract form of the quotient is *Positivity and the Positive Cone of a Hermitian Form*, §*The Definite Quotient*, and the article states it here only to record that it uses no definiteness assumption beyond the positivity.

## The Passage from Positivity to Continuity

### The Continuity Is the Boundedness of the Diagonal

**Theorem (the reduction to the diagonal).** Let $s$ be Hermitian and positive semi-definite on a normed module, with values in $R$. Then $s$ is continuous iff its diagonal is bounded on the unit ball, and in that case

$$
\lVert s\rVert = \sup\{\lvert s(x,y)\rvert : \lVert x\rVert \leq 1, \lVert y\rVert \leq 1\} = \sup\{s(x,x) : \lVert x\rVert \leq 1\} .
$$

*Proof.* If $s(x,x) \leq M\lVert x\rVert^{2}$ for every $x$, then the inequality gives $\lvert s(x,y)\rvert^{2} \leq s(x,x)s(y,y) \leq M^{2}\lVert x\rVert^{2}\lVert y\rVert^{2}$, hence $\lvert s(x,y)\rvert \leq M\lVert x\rVert\lVert y\rVert$ and $\lVert s\rVert \leq M$; conversely $\lvert s(x,x)\rvert \leq \lVert s\rVert\lVert x\rVert^{2}$ by the definition of the bound, and $s(x,x) \geq 0$. The two suprema therefore agree at $M = \sup_{\lVert x\rVert \leq 1}s(x,x)$. $\square$

**Corollary (the continuity of the layer's forms is one scalar condition).** On the objects of the layer the form is continuous by hypothesis, *Topological Sesqualgebras with a Form*, §*The Definition*, so the diagonal is bounded and the inequality holds with the constant $\lVert s\rVert$; in the **definite** case the bound is free of the hypothesis, since the norm of the form gives $\lvert s(x,y)\rvert \leq \lVert x\rVert\lVert y\rVert$ with constant one, *The Norm Defined by a Form*, §*The Boundedness of the Form*; and for the **canonical pairing** $s(x,y) = y^{*}x$ of a $\mathrm{C}^{*}$-sesqualgebra the diagonal has $s(x,x) = x^{*}x$ of norm $\lVert x\rVert^{2}$, so the bound is the $\mathrm{C}^{*}$-identity and is free. The passage from positivity to continuity is thus the passage from the pointwise inequality $s(x,x) \geq 0$ to the global one $s(x,x) \leq M\lVert x\rVert^{2}$.

### The Boundedness Is Not Free

**Example (a positive form that is not continuous).** Let $A = \mathbb{C}[x]$ with the supremum norm on $[0,1]$ and let $\varphi$ be the linear functional with $\varphi(x^{n}) = n!$, well defined and everywhere finite on the polynomials since every element is a finite combination of the monomials. Then

$$
s(p,q) = \varphi(p)\,\varsigma(\varphi(q))
$$

is Hermitian and positive semi-definite — the diagonal is $s(p,p) = \lvert\varphi(p)\rvert^{2} \geq 0$ — and it is not continuous: $\lVert x^{n}\rVert = 1$ while $s(x^{n},x^{n}) = (n!)^{2}$, so the diagonal is unbounded on the unit ball and the inequality of the preceding theorem has no finite constant. The example is the witness that positivity alone does not bound the diagonal, hence does not give continuity, and it is the reason the article states the boundedness of the diagonal as the hypothesis and does not claim the automatic continuity that the layer does not have.

**Remark (where the continuity is free).** On a unital $\mathrm{C}^{*}$-algebra the boundedness of a positive functional is free and the bound is $\lVert f\rVert = f(1)$, *States and Positive Functionals on a Topological Sesqualgebra*, §*The Cauchy–Schwarz Inequality and the Null Space*; on an arbitrary unital Banach sesqualgebra it is not, as that article's remark records, and the layer accordingly restricts to the continuous maps. The example above is the corresponding witness for a general positive map, and the two together are the reason the article's hypotheses are the continuity of the map and its positivity, neither implying the other.

## The $\mathrm{C}^{*}$-Valued Maps

### The Norm Inequality

**Theorem (the $\mathrm{C}^{*}$-valued norm inequality).** Let $s : A \times A \to B$ be Hermitian and positive semi-definite with values in a $\mathrm{C}^{*}$-algebra $B$, and let the module carry a norm. Then

$$
\lVert s(x,y)\rVert^{2} \leq \lVert s(x,x)\rVert\,\lVert s(y,y)\rVert \qquad \text{for all } x, y .
$$

*Proof.* For a state $\omega$ of $B$ the composite $\omega \circ s$ is a Hermitian positive semi-definite form with values in $\mathbb{C}$, by the proposition on the scalar reductions, so Cauchy–Schwarz applies to it: $\lvert\omega(s(x,y))\rvert^{2} \leq \omega(s(x,x))\,\omega(s(y,y)) \leq \lVert s(x,x)\rVert\lVert s(y,y)\rVert$. A state is a positive functional of norm one, and $\lVert b\rVert = \sup\{\lvert\omega(b)\rvert : \omega \text{ a state}\}$ for a $\mathrm{C}^{*}$-algebra element $b$, so taking the supremum over the states gives the claim. $\square$

**Remark (the sharp algebraic form is the module case).** The inequality of the theorem is the norm form; the sharper algebraic form

$$
s(y,x)\,s(x,y) \leq \lVert s(x,x)\rVert\,s(y,y),
$$

in which the product in $B$ replaces the product of the norms, holds when $s$ is an inner product in the module sense, $s(x,ya) = s(x,y)a$; it is the Cauchy–Schwarz inequality of a Hilbert $\mathrm{C}^{*}$-module, *Hilbert and $\mathrm{C}^{*}$-Modules*, §*The $A$-valued norm*, and its proof uses the $A$-linearity of the second slot in the choice of the parameter. For a general positive sesquilinear map, which has no module structure, the norm form above is what the scalar reductions give, and it is the form that the operator layers use.

### The Canonical Pairing

**Theorem (the canonical pairing).** Let $A$ be a $\mathrm{C}^{*}$-sesqualgebra over $(\mathbb{C},\varsigma)$ and let $s(x,y) = y^{*}x$, the universal $A$-valued form $\Psi$ of *Hermitian Forms on a Sesqualgebra*, §*The Reduction to the Scalars*. Then $s$ is a Hermitian positive semi-definite $A$-valued sesquilinear map in the layer's convention, with

$$
s(x,x) = x^{*}x, \qquad \lVert s(x,x)\rVert = \lVert x\rVert^{2}, \qquad \lVert s(x,y)\rVert \leq \lVert x\rVert\lVert y\rVert ,
$$

its radical is zero, because $y^{*}x = 0$ at $y = x$ gives $x^{*}x = 0$ and hence $x = 0$, and its scalar reductions along the positive functionals are the conjugates of their pairings, $f(y^{*}x) = \overline{f(x^{*}y)} = \varsigma(h_{f}(x,y))$.

*Proof.* The two slot rules are $s(\lambda x,y) = y^{*}(\lambda x) = \lambda\,s(x,y)$ and $s(x,\lambda y) = (\lambda y)^{*}x = \varsigma(\lambda)s(x,y)$, which is the layer's convention; the map is Hermitian, $s(y,x) = x^{*}y = (y^{*}x)^{*} = s(x,y)^{*}$; it is positive, $s(x,x) = x^{*}x \geq 0$ in the $\mathrm{C}^{*}$-order; its diagonal has $\lVert s(x,x)\rVert = \lVert x^{*}x\rVert = \lVert x\rVert^{2}$ by the $\mathrm{C}^{*}$-identity, so the bound of the theorem above is the constant one; and the radical vanishes because $y^{*}x = 0$ for $y = x$ is $x^{*}x = 0$, which forces $x = 0$ in a $\mathrm{C}^{*}$-algebra. The pairing $h_{f}$ of *States and Positive Functionals on a Topological Sesqualgebra*, §*The Sesquilinear Pairing*, reads the same form in the Hilbert convention, conjugate-linear in the first slot, $h_{f}(x,y) = f(x^{*}y) = \varsigma(f(y^{*}x))$. $\square$

**Remark (the scalar theory of the layer is the reducible part of the operator theory).** The theorem is the sense in which the scalar forms of the layer, which are the reductions $h_{\varphi}(x,y) = \varphi(y^{*}x)$ of *The Sesquilinear Form and the Conjugation*, are the scalar readings of the one $A$-valued form $\Psi(x,y) = y^{*}x$; the inequality of this article is the common inequality of the two readings, and the operator theory of the two forms is *Adjoints of Bounded Sesquilinear Operators* and *The Adjoint of the Bounded Conjugate Left Multiplication*.

## The Collapse at the Trivial Involution

**Theorem (the collapse).** Let $\varsigma = \mathrm{id}$, so that $R = k$ is an ordered field and the sesquilinear maps are $k$-bilinear. Then the Cauchy–Schwarz inequality reads

$$
s(x,y)^{2} \leq s(x,x)\,s(y,y)
$$

for a positive semi-definite symmetric bilinear form, the modulus is the absolute value, the seminorm is the square root of the diagonal, the null set is the radical, and the equality case is proportionality modulo the radical. The article is then the classical Cauchy–Schwarz inequality of a positive semi-definite symmetric bilinear form, and its instance on a Euclidean space is the scalar theory of *Bilinear Forms* and *Quadratic Forms and Polarisation*.

*Proof.* Each statement is the corresponding statement above read at $\varsigma = \mathrm{id}$: the Hermitian property is the symmetry, the modulus square is the square, and the two slots carry the same scalars. $\square$

**Remark (which statements are sesquilinear).** The inequality, the seminorm, the quotient and the equality case hold in both kinds and are not sesquilinear statements; the sesquilinear content is the presence of two slots with different scalar rules, which is what makes the inequality read $\varsigma(s(x,y))s(x,y)$ rather than $s(x,y)^{2}$, the degenerate case require the vanishing of both the real and the imaginary part of $s(x,y)$, and the modulus $\lvert s(x,y)\rvert = (s(x,y)\varsigma(s(x,y)))^{1/2}$ appear in the bound.

## Examples

### The Pairing of a Positive Functional

**Example (the functional pairing).** Let $f$ be a positive functional on a unital $\mathrm{C}^{*}$-sesqualgebra and let $s(x,y) = f(y^{*}x)$. The form is Hermitian and positive semi-definite, its diagonal is $f(x^{*}x)$, the inequality is $\lvert f(y^{*}x)\rvert^{2} \leq f(x^{*}x)f(y^{*}y)$, the seminorm is $p(x) = f(x^{*}x)^{1/2}$, its null set is the left ideal $N_{f}$ of the functional, and the quotient is the inner product space whose completion carries the GNS representation. The example is the model of the article and is developed as *States and Positive Functionals on a Topological Sesqualgebra*, §*The Cauchy–Schwarz Inequality and the Null Space*; the continuity there is free with $\lVert f\rVert = f(1)$.

### The Matrix Algebra

**Example (the Frobenius form).** On $A = M_{n}(\mathbb{C})$ with the trace form $s(X,Y) = \operatorname{tr}(XY^{*})$ the form is Hermitian, positive definite and nondegenerate, the inequality is $\lvert\operatorname{tr}(XY^{*})\rvert^{2} \leq \operatorname{tr}(XX^{*})\operatorname{tr}(YY^{*})$, which is the Cauchy–Schwarz inequality for the Frobenius inner product, and the seminorm is the Frobenius norm whose boundedness is the continuity of the form with constant one, *The Norm Defined by a Form*, §*The Matrix Algebra*. The example is the definite model in which the inequality is sharp and the continuity is free.

### The Biquaternion Algebra

**Example (the definite and the indefinite forms).** On the biquaternion algebra $\mathbb{B}$ the general plain sesquilinear form

$$
h(\tilde{P},\tilde{Q}) = \operatorname{Sc}(\tilde{P}\tilde{Q}^{*}) = \sum_\mu P_\mu\,\varsigma(Q_\mu)
$$

is Hermitian, compatible, nondegenerate and positive definite, so the inequality holds for it with the diagonal $\sum_\mu\lvert Q_\mu\rvert^{2}$ and the constant one, the seminorm being the Euclidean norm of *The Norm Defined by a Form*, §*The Biquaternion Trace Form*. The general quaternionic sesquilinear pairing $\operatorname{Sc}(\tilde{P}^{\natural}\tilde{Q}^{*})$, of signature $(2,6)$, is indefinite, and for it the inequality **fails**: it is the caution of *The Indefinite Case and the Signature*, §*The Biquaternion Caution*, and the example separates the positive semi-definite hypothesis of the article from the Hermitian one. The two forms are the forms of *The Four Pairings of the Biquaternion Algebra* and *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

### The Unbounded Positive Form

**Example (positivity without continuity).** The rank-one form $s(p,q) = \varphi(p)\varsigma(\varphi(q))$ of the unbounded functional $\varphi(x^{n}) = n!$ on $\mathbb{C}[x]$ with the supremum norm is the witness of the article: it is positive semi-definite and Hermitian with the diagonal $s(p,p) = \lvert\varphi(p)\rvert^{2}$, and the diagonal is unbounded on the unit ball, so the form is not continuous and the article's inequality has no constant. The example is the counterpart, for a general positive sesquilinear map, of the remark that the boundedness of a positive functional on a Banach sesqualgebra is not automatic.

## Summary

A Hermitian **positive** sesquilinear map satisfies the Cauchy–Schwarz inequality without any definiteness assumption: with values in the base it reads $\varsigma(s(x,y))s(x,y) \leq s(x,x)s(y,y)$ in the fixed field, equivalently $\lvert s(x,y)\rvert^{2} \leq s(x,x)s(y,y)$, and it is proved by translating one argument by $\mu = s(x,y)/s(y,y)$ and using that the translated diagonal $s(x,x) - \lvert s(x,y)\rvert^{2}/s(y,y)$ is $\geq 0$; the case $s(y,y) = 0$ is not exceptional, the translated quadratic in a real parameter forcing $s(x,y) = 0$, so the neutral element lies in the radical. The inequality is an equality exactly for the pairs dependent modulo the radical, so the definite case of *The Norm Defined by a Form* is the sharp case of the general one. The **seminorm** $p(x) = s(x,x)^{1/2}$ has the triangle inequality from the inequality itself, $\lvert s(x,y)\rvert \leq p(x)p(y)$, and its null set is the **radical**, which is why the positive semi-definite form that is not definite defines a seminorm and the definite quotient is an inner product whose completion is a Hilbert space; the identification of the null set with the radical is *Positivity and the Positive Cone of a Hermitian Form*, §*The Null Set and the Radical*, and it uses the inequality of this article. The **passage from positivity to continuity** is the reduction of the continuity of the map to the boundedness of the single function $s(x,x)$ on the unit ball, with $\lVert s\rVert = \sup_{\lVert x\rVert \leq 1}s(x,x)$; that boundedness is free in the definite case with constant one, free for the canonical pairing $s(x,y) = y^{*}x$ of a $\mathrm{C}^{*}$-sesqualgebra where $\lVert s(x,x)\rVert = \lVert x\rVert^{2}$, free for a positive functional on a unital $\mathrm{C}^{*}$-algebra where the bound is $f(1)$, and **not** free in general, the rank-one form of an unbounded functional on $\mathbb{C}[x]$ with the supremum norm being the witness that positivity alone does not bound the diagonal. For values in a $\mathrm{C}^{*}$-algebra the scalar reductions along the states reduce the inequality to the scalar case and give $\lVert s(x,y)\rVert^{2} \leq \lVert s(x,x)\rVert\lVert s(y,y)\rVert$, with the sharper algebraic form $s(y,x)s(x,y) \leq \lVert s(x,x)\rVert s(y,y)$ in the module case of *Hilbert and $\mathrm{C}^{*}$-Modules*. At $\varsigma = \mathrm{id}$ the inequality is the classical one for a positive semi-definite symmetric bilinear form, and the sesquilinear content is the two slot rules, the degenerate case and the modulus. The examples are the pairing of a positive functional, the Frobenius form, the definite and the indefinite forms on the biquaternion algebra, and the unbounded positive form.

## Summary of Notation

| symbol | meaning |
|---|---|
| $s(x,y)$, $s(y,x) = \varsigma(s(x,y))$ | a Hermitian sesquilinear map with values in the base; the exchange conjugates the value |
| $s(\lambda x,y) = \lambda s(x,y)$, $s(x,\lambda y) = \varsigma(\lambda)s(x,y)$ | the two slot rules; linear in the first, semilinear in the second |
| $s(x,x) \in k$ | the diagonal, in the fixed field; $\geq 0$ for a positive map |
| $\varsigma(s(x,y))s(x,y) \leq s(x,x)s(y,y)$ | the Cauchy–Schwarz inequality, no definiteness assumed |
| $s(x-\mu y,x-\mu y) = s(x,x) - \lvert s(x,y)\rvert^{2}/s(y,y)$, $\mu = s(x,y)/s(y,y)$ | the translated diagonal with which the inequality is proved |
| $s(y,y) = 0 \Rightarrow s(x,y) = 0$ | the degenerate case, and the containment of the neutral element in the radical |
| equality $\iff$ dependent modulo the radical | the equality case; proportionality in the definite case |
| $p(x) = s(x,x)^{1/2}$, $\lvert s(x,y)\rvert \leq p(x)p(y)$ | the seminorm of the form and the inequality as its triangle inequality |
| $\{s(x,x) = 0\} = \mathrm{rad}(s)$ | the null set is the radical; the seminorm is a norm exactly on the definite quotient |
| $\lVert s\rVert = \sup_{\lVert x\rVert \leq 1}s(x,x)$ | continuity is the boundedness of the diagonal, for a positive map |
| $\lVert s(x,y)\rVert^{2} \leq \lVert s(x,x)\rVert\lVert s(y,y)\rVert$ | the $\mathrm{C}^{*}$-valued inequality, by reduction along the states |
| $s(y,x)s(x,y) \leq \lVert s(x,x)\rVert s(y,y)$ | the sharp algebraic form, in the module case |
| $s(x,y) = y^{*}x$, $\lVert s(x,x)\rVert = \lVert x\rVert^{2}$ | the canonical $A$-valued pairing, continuous by the $\mathrm{C}^{*}$-identity |
| $s(p,q) = \varphi(p)\varsigma(\varphi(q))$, $\varphi(x^{n}) = n!$ | the unbounded positive form: positivity without continuity |
| $\varsigma = \mathrm{id}$ | the collapse: $s(x,y)^{2} \leq s(x,x)s(y,y)$, the classical symmetric case |

## Further Reading

- Gérard J. Murphy, *$\mathrm{C}^{*}$-Algebras and Operator Theory* (Academic Press, 1990), for the positivity, the Cauchy–Schwarz inequality of a positive functional and the GNS construction.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the positive forms on a normed space and the boundedness questions.
- E. Christopher Lance, *Hilbert $\mathrm{C}^{*}$-Modules: A Toolkit for Operator Algebraists* (Cambridge University Press, 1995), for the $\mathrm{C}^{*}$-valued inner products and their Cauchy–Schwarz inequality.
- William L. Paschke, *Inner product modules over $B^{*}$-algebras* (Transactions of the American Mathematical Society 182, 1973), for the $\mathrm{C}^{*}$-valued Cauchy–Schwarz inequality and the module case.
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for the scalar Cauchy–Schwarz inequality, its equality case and the completion of an inner product space.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the positive semi-definite forms over an ordered field with involution and their radical.
- Konrad Schmüdgen, *Unbounded Self-Adjoint Operators on Hilbert Space* (Springer, 2012), for the positive forms that are not bounded and the operator theory they support.
