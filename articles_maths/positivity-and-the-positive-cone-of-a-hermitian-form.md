# __Positivity and the Positive Cone of a Hermitian Form__

## Introduction

A Hermitian form on a sesqualgebra takes its diagonal values in the fixed ring $R^{\varsigma}$ of the base involution, by the proposition (the diagonal) of *Topological Sesqualgebras with a Form*, §*The Form*, and once that ring is ordered the diagonal can be compared with zero. **Positivity** is the sign of the diagonal: the form is **positive semi-definite** when $h(x,x) \geq 0$ for every $x$ and **positive definite** when $h(x,x) > 0$ for every $x \neq 0$, with the negative and the indefinite cases read by the same rule. The setting is the layer of *Topological Sesqualgebras with a Form*, so the form is continuous, Hermitian and compatible with the product, and the positivity is a property of the form and of the order of the base; no norm enters, the norm that a definite form defines being *The Norm Defined by a Form*.

Three facts organise the article. **The positive semi-definite forms form a cone.** They are closed under addition and under the nonnegative scalars of the fixed ring, so the positive semi-definite forms are a cone in the module of the Hermitian forms, which is the sense in which positivity is a cone condition and not a list of inequalities. **The relation that the form defines**, $x \succeq y$ when $h(x-y,x-y) \geq 0$, is reflexive, symmetric and translation invariant: it is a **tolerance** on $A$ and not an order, it is transitive exactly for the semi-definite forms, and the obstruction to being more than a congruence is the **null set** $\{x : h(x,x) = 0\}$, which for a positive semi-definite form coincides with the radical. The genuine order of the layer is on the Hermitian elements and is the cone of the Hermitian squares, read by the positive functionals. And **positivity of the form is positivity of a functional on the algebraic cone**. For the form $h_{\varphi}(x,y) = \varphi(y^{*}x)$ of *The Sesquilinear Form and the Conjugation*, §*The Correspondence*, the diagonal is $h_{\varphi}(x,x) = \varphi(x^{*}x)$, so $h_{\varphi}$ is positive semi-definite exactly when $\varphi$ is nonnegative on the cone of the Hermitian squares of *Hermitian Squares and the Algebraic Positive Cone*, and positive definite exactly when $\varphi$ is strictly positive on its nonzero elements, which is the properness criterion of that article. A definite form is therefore a certificate that the algebraic cone is proper.

The article defines the four kinds and the cone of the positive semi-definite forms, reads the tolerance and the two sets that it and the diagonal define, proves that the null set is the radical in the positive semi-definite case, descends the form to the definite quotient by the radical, reduces the positivity to the positivity of a functional on the algebraic cone, and compares the result with the bilinear layer, with the collapse closing the article. The scalar forms and the correspondence are *The Sesquilinear Form and the Conjugation*, the compatibility, the radical and the nondegeneracy *Topological Sesqualgebras with a Form*, the inequality that identifies the null set and the radical *The Cauchy–Schwarz Inequality for Continuous Sesquilinear Maps*, the norm and the triangle inequality *The Norm Defined by a Form*, the signature and the indefinite classification *The Indefinite Case and the Signature*, the algebraic cone and its order *Hermitian Squares and the Algebraic Positive Cone*, and the positive functionals *States and Positive Functionals on an Involutive Algebra*, *The Cone of Positive Functionals* and *Positive Definite Forms and the Order*, where the construction of the Hilbert space from a definite form belongs. Throughout, $R$ is an ordered commutative ring with $1$, $\varsigma$ is an order-preserving involution of it so that the fixed ring $R^{\varsigma}$ is an ordered subring, $A$ is an associative $R$-algebra with $1$ and a $\varsigma$-semilinear involution $*$, and $h$ is a Hermitian form on $A$ compatible with the product in the sense of the entry.

## The Sign of the Diagonal

### The Four Kinds

**Definition.** Let $h$ be a Hermitian form with values in the ordered ring $R^{\varsigma}$ on the diagonal. Say that $h$ is

$$
\begin{aligned}
&\textbf{positive semi-definite} && \text{when } h(x,x) \geq 0 \text{ for every } x , \\
&\textbf{positive definite} && \text{when } h(x,x) > 0 \text{ for every } x \neq 0 , \\
&\textbf{negative semi-definite} && \text{when } h(x,x) \leq 0 \text{ for every } x , \\
&\textbf{negative definite} && \text{when } h(x,x) < 0 \text{ for every } x \neq 0 .
\end{aligned}
$$

A Hermitian form that is neither positive semi-definite nor negative semi-definite is **indefinite**.

**Remark.** The four definitions are the two signs read on the diagonal alone, and they are related by the involution of the sign: $h$ is negative semi-definite exactly when $-h$ is positive semi-definite, and negative definite exactly when $-h$ is positive definite. A definite form, positive or negative, has no nonzero isotropic vector, $h(x,x) = 0$ forcing $x = 0$; the converse fails in general, because an indefinite form can have no nonzero isotropic vector, as $x_{1}^{2} - 2x_{2}^{2}$ over $\mathbb{Q}$ shows, and the set of the isotropic vectors is the object of the next section. The indefinite forms are the complement of the two semi-definite classes, and their classification by inertia and signature is *The Indefinite Case and the Signature*.

### The Diagonal

**Proposition (the diagonal is a fixed scalar and scales by squares).** For every $x$ the value $h(x,x)$ lies in $R^{\varsigma}$, and for every $\lambda \in R^{\varsigma}$,

$$
h(\lambda x, \lambda x) = \lambda^{2}\,h(x,x) .
$$

*Proof.* The fixed ring is the proposition (the diagonal) of the entry, §*The Form*. For the scaling, $h(\lambda x, \lambda x) = \lambda\,\varsigma(\lambda)\,h(x,x)$ by the two slot rules, and $\varsigma(\lambda) = \lambda$ because $\lambda$ is fixed, so the product is $\lambda^{2}h(x,x)$. $\square$

**Remark.** The scaling by the square is what makes the fixed ring the natural ring of scalars for the sign: an ordered ring has $\lambda^{2} \geq 0$ for every $\lambda$, so the positivity of the diagonal is preserved by every scalar of $R^{\varsigma}$ and a scalar with $\lambda^{2} = 0$ and $\lambda \neq 0$ is excluded by the order. The polarisation of the diagonal is $h(x+y,x+y) - h(x,x) - h(y,y) = h(x,y) + h(y,x)$, the two mixed terms that a scalar reduction would read as $h(x,y) + \varsigma(h(x,y))$.

### The Cone of Positive Forms

**Theorem.** The positive semi-definite forms are closed under addition and under multiplication by the elements $\lambda \in R^{\varsigma}$ with $\lambda \geq 0$. Consequently they form a convex cone in the $R^{\varsigma}$-module of the Hermitian forms, and the same holds for the negative semi-definite forms with the sign reversed.

*Proof.* Let $h, h'$ be positive semi-definite and let $\lambda, \mu \in R^{\varsigma}$ with $\lambda, \mu \geq 0$. The form $\lambda h + \mu h'$ is biadditive and Hermitian, because a fixed scalar commutes with $\varsigma$, and its diagonal is $(\lambda h + \mu h')(x,x) = \lambda h(x,x) + \mu h'(x,x)$, a sum of nonnegative elements of the ordered ring, hence nonnegative. The negative case is the sign reversed. $\square$

**Remark.** The closure under addition uses only the addition of the values, and it is the reason the phrase "the positive cone of the forms" is available: the positive semi-definite forms are the cone of the Hermitian forms at the sign $+$, the negative semi-definite ones its opposite, and a definite form is a point of the cone that is strictly positive on the nonzero elements, so the definite forms are the part of the cone cut out by the strict inequality $h(x,x) > 0$ for $x \neq 0$. The cone is a statement about the diagonal alone and needs no hypothesis beyond the order; in particular it neither needs nor implies the nondegeneracy of its members.

## The Relation Defined by the Form

### The Tolerance

**Definition.** For $x, y \in A$ write $x \succeq y$ when $h(x-y,x-y) \geq 0$.

**Proposition.** The relation $\succeq$ is reflexive, symmetric and invariant under translation: $x \succeq x$ for every $x$; from $x \succeq y$ follows $y \succeq x$; and from $x \succeq y$ follows $x + z \succeq y + z$ for every $z$.

*Proof.* Reflexivity is $h(0,0) = 0 \geq 0$. Symmetry is the invariance of the diagonal under the sign: $h(y-x,y-x) = h(-(x-y),-(x-y)) = h(x-y,x-y)$, because $h(-u,-v) = (-1)\varsigma(-1)h(u,v) = h(u,v)$ by the two slot rules and $\varsigma(-1) = -1$. Translation adds the same $z$ to the two members and leaves the difference unchanged. $\square$

**Remark (it is not an order).** The relation is symmetric, so it is antisymmetric exactly when it is the equality of $A$, that is when the form is negative definite, and otherwise it is a **tolerance** on $A$ and not an order; the phrase "the order of the form" must be read with that caution. What the form orders is not the module but the cone of the Hermitian squares of the algebra and the cone of its positive functionals, as the section on the algebraic cone records; the tolerance records only the sign of the diagonal of a difference.

### Transitivity and the Null Set

**Definition.** The **null set** of the form is

$$
N(h) = \{x \in A : h(x,x) = 0\} .
$$

**Proposition.** The tolerance is transitive when the form is semi-definite, and it fails when the form is indefinite. For a positive semi-definite form it is the total relation, every pair being related; for a negative semi-definite one it is the congruence $x \succeq y \iff x - y \in N(h)$; for an indefinite one it is not transitive, and the witness is in the last section.

*Proof.* For a positive semi-definite form $h(x-y,x-y) \geq 0$ for every pair, so every pair is related and transitivity is trivial. For a negative semi-definite form $h(u,u) \leq 0$ for every $u$, so $x \succeq y$ says $h(x-y,x-y) \geq 0$ and $\leq 0$, that is $x - y \in N(h)$; now $N(h)$ is the radical for a semi-definite form by the theorem of the next section, applied to $h$ in the positive case and to $-h$ in the negative one, so it is a subspace and the relation is the congruence by a subspace, which is transitive. The failure in the indefinite case is the example of the last section. $\square$

**Remark.** The three regimes are the trivial one, the congruence by the null set and the failure, so the tolerance carries order-like information only in the semi-definite cases, and even there it is an equivalence on the quotient rather than an order on the module. The genuine order of the layer is on the **Hermitian elements** of the algebra, and it is read by the positive functionals: the cone of the Hermitian squares of *Hermitian Squares and the Algebraic Positive Cone*, §*The Order* is the positive cone of the Hermitian part, and *Positive Definite Forms and the Order* recovers it as the intersection of the half-spaces cut by the positive functionals.

### The Positive Set

**Definition.** The **positive set** of the form is $P(h) = \{x \in A : h(x,x) \geq 0\}$.

**Proposition.** The positive set contains $0$, it is stable under the scalars of the fixed ring, and

$$
P(h) \cap (-P(h)) = N(h) .
$$

Consequently $h$ is positive semi-definite exactly when $P(h) = A$, and the positive set is proper, $P(h) \cap (-P(h)) = \{0\}$, exactly when the form is anisotropic, that is when it has no nonzero isotropic vector; definiteness is the stronger condition that also fixes the sign.

*Proof.* The element $0$ is positive because $h(0,0) = 0$. Stability under $\lambda \in R^{\varsigma}$ is the scaling $h(\lambda x,\lambda x) = \lambda^{2}h(x,x) \geq 0$ of the proposition above. For the intersection, $x \in P(h) \cap (-P(h))$ says $h(x,x) \geq 0$ and $h(-x,-x) = h(x,x) \leq 0$, that is $h(x,x) = 0$; this is exactly $x \in N(h)$. The identification $P(h) = A$ is the definition of the positive semi-definite case, and the properness statement is the same identification read on the null set. $\square$

**Remark (the positive set is not a cone in general).** $P(h)$ is stable under the scalars of $R^{\varsigma}$ and it satisfies the properness relation above, but it is not closed under addition unless $h$ is positive semi-definite, in which case it is all of $A$: for an indefinite form the two mixed terms of $h(x+y,x+y)$ can bring the value below zero, as the example of the last section shows. The set is therefore a genuine subset of $A$ for an indefinite form, and the word "cone" applied to it records its closure under the nonnegative scalars alone; the cone of the forms of the previous section is a cone in the strict sense, and the two must not be confused.

**Remark (the radical is inside the null set).** The radical $A^{\perp}$ of the entry is contained in $N(h)$: if $h(x,y) = 0$ for every $y$ then in particular $h(x,x) = 0$. The inclusion can be strict for an indefinite form and is an equality for a positive semi-definite one, by the Cauchy–Schwarz inequality of the next section.

## The Radical and the Definite Quotient

### The Null Set and the Radical

**Theorem.** Let $h$ be positive semi-definite. Then

$$
N(h) = A^{\perp} ,
$$

the null set is the radical, it is a subspace of $A$, and $h$ is positive definite exactly when its radical vanishes.

*Proof.* The inclusion $A^{\perp} \subseteq N(h)$ is the remark above. For the converse let $h(x,x) = 0$ and let $y$ be arbitrary. The Cauchy–Schwarz inequality of *The Cauchy–Schwarz Inequality for Continuous Sesquilinear Maps*, in the algebraic form $\varsigma(h(x,y))\,h(x,y) \leq h(x,x)\,h(y,y)$ with its equality case, gives $\varsigma(h(x,y))h(x,y) \leq 0$ on the right, while the left side is a product of a fixed scalar with its conjugate and is $\geq 0$; the two together put the left side at zero, and the equality case of the cited inequality then gives $h(x,y) = 0$. So $h(x,y) = 0$ for every $y$ and $x \in A^{\perp}$. For the last clause, $h$ is positive definite exactly when $N(h) = \{0\}$, which by the equality is the vanishing of the radical. $\square$

**Remark.** The theorem is the reason the null set and the radical are not distinguished in the positive semi-definite case, and the reason they must be distinguished in general: for an indefinite form the radical is strictly smaller, and the example of the last section exhibits a nondegenerate indefinite form whose null set is a pair of lines. The cited inequality is the only place where the hypothesis of positive semi-definiteness is used, and it is used in the sharp form of the equality case.

### The Definite Quotient

**Theorem.** Let $h$ be positive semi-definite and let $A^{\perp}$ be its radical. Then $h$ descends to the quotient $A/A^{\perp}$ of the underlying module and the descended form is positive definite.

*Proof.* The radical is a left ideal by *Topological Sesqualgebras with a Form*, §*The Radical Is an Ideal*, hence a submodule, and the descent of the form needs only the containment $A^{\perp} \subseteq \operatorname{rad}(h)$, which is the definition of the radical: for $j \in A^{\perp}$ the two values are $h(x+j,y) = h(x,y)$ and $h(x,y+j) = h(x,y) + h(x,j)$ with $h(x,j) = \varsigma(h(j,x)) = 0$. The diagonal of the descended form is the descended diagonal, so it is positive semi-definite, and its radical is the radical of the quotient, which is zero because the preimage of the radical of the quotient is the radical of $A$, and the radical of $A$ is exactly the submodule divided out. A positive semi-definite form with zero radical is positive definite by the theorem above. $\square$

**Remark (the quotient is a module, not an algebra, in general).** The descent uses only that the radical is a submodule. For the quotient to inherit the algebra structure and the involution, the radical must be two-sided and $*$-stable, and that is not automatic: *Topological Sesqualgebras with a Form*, §*The Radical Is an Ideal* records only a left ideal whose image under $*$ is a right ideal, and the asymmetry is real. On $M_2(\mathbb{Q})$ with the transpose and $\varphi(X) = X_{11}$ the form $h(X,Y) = (Y^{T}X)_{11}$ is Hermitian and compatible, its radical is the set of matrices with first column zero, a left ideal which is not a right ideal, because $X = E_{12}$ lies in the radical while $X \cdot (E_{21} + E_{22}) = E_{11} + E_{12}$ does not, $h(E_{11}+E_{12}, E_{11}+E_{12}) = 1$; and the radical is not $*$-stable, its image being the matrices with first row zero. The form therefore descends without the algebra, and the quotient is an algebra with the induced involution exactly when the radical is an invariant ideal, which is the hypothesis of *Hermitian Forms on a Sesqualgebra*, §*The Induced Form on a Quotient*.

**Corollary (the quotient is the definite quotient).** For a positive semi-definite form the quotient of $A$ by the null set is the largest quotient on which the form is positive definite, and it is the quotient by the radical.

*Proof.* The null set is the radical by the theorem above, so the quotient is $A/A^{\perp}$, and any quotient on which the form is positive definite has the radical of $A$ in the kernel of the class map, because an element of the radical is annihilated by every value of the form. $\square$

**Remark.** The quotient is the definite reduction of the pair, and it is the algebraic shadow of the passage from a positive semi-definite form to the Hilbert space of *Positive Definite Forms and the Order*; the construction of the space, the completion and the representation belong to that article and to the analysis layer, and this article stops at the quotient, where the tolerance of the previous section becomes the total relation and carries no order-like information. The order itself, on the Hermitian elements, is the one of the algebraic cone.

## The Algebraic Cone and the Positive Functionals

### The Diagonal of the Reduction

**Theorem.** Let $\varphi : A \to R$ be $R$-linear and let $h_{\varphi}(x,y) = \varphi(y^{*}x)$ be the corresponding compatible form. Then

$$
h_{\varphi}(x,x) = \varphi(x^{*}x) = \varphi(\Psi(x,x)) ,
$$

with $\Psi$ the $A$-valued form of *Hermitian Forms on a Sesqualgebra*, and consequently $h_{\varphi}$ is positive semi-definite if and only if $\varphi$ is nonnegative on the algebraic cone $C(A)$ of the Hermitian squares, and positive definite if and only if $\varphi$ is strictly positive on the nonzero elements of $C(A)$.

*Proof.* The diagonal is $h_{\varphi}(x,x) = \varphi(x^{*}x)$ by the definition, and $x^{*}x = \Psi(x,x)$ is the diagonal of the $A$-valued form. A finite sum $\sum_{i}x_{i}^{*}x_{i}$ of Hermitian squares has $\varphi$-value $\sum_{i}\varphi(x_{i}^{*}x_{i})$ by the additivity of $\varphi$, so $\varphi \geq 0$ on all the squares is equivalent to $\varphi \geq 0$ on the cone they generate, which is the positive semi-definite case read on the diagonal. For the definite case, $h_{\varphi}(x,x) > 0$ for every $x \neq 0$ says $\varphi(x^{*}x) > 0$ for every $x \neq 0$; a nonzero element $c = \sum_i x_i^{*}x_i$ of the cone has at least one $x_i \neq 0$, so $\varphi(c) \geq \varphi(x_i^{*}x_i) > 0$, and conversely the strict positivity on the cone restricts to the nonzero squares. $\square$

### The Properness Certificate

**Corollary.** If there exists a positive definite form $h_{\varphi}$ on $A$, then the algebraic cone $C(A)$ is proper, and $\varphi$ is strictly positive on every nonzero element of the cone.

*Proof.* The functional $\varphi$ is additive with values in the ordered ring $R$, it is nonnegative on every Hermitian square and strictly positive on every nonzero square, which is the sufficient criterion for properness of *Hermitian Squares and the Algebraic Positive Cone*, §*Properness*; the strict positivity on the whole cone is the last part of that criterion. $\square$

**Remark.** The corollary is the precise sense in which positivity of a form is a certificate about the algebra: the form measures the cone, and the existence of one form that is strictly positive on the nonzero squares makes the cone proper. The converse is not claimed: a proper cone need not carry a functional strictly positive on it, and the criterion of the cited article is sufficient and not necessary, so the existence of a definite form is a strong condition on the pair.

### The Boundary with the Positive Functionals

**Remark.** The functionals $\varphi$ that are nonnegative on the cone are the **positive functionals** of *States and Positive Functionals on an Involutive Algebra*, their cone is *The Cone of Positive Functionals* and *The Positive Cone of an Involutive Algebra*, and the Hilbert space, the representation and the vector states they build are *Positive Definite Forms and the Order* and *Positive Definite Forms on an Ordered Space*, in the analysis layer. This article keeps the elementary layer: the sign of the diagonal, the order, the null set and the quotient, with the functional reduced to its values on the cone of the squares.

## The Bilinear Comparison

### The Symmetric Case

**Proposition.** Let $\varsigma = \mathrm{id}$. Then the form is $R$-bilinear and symmetric, $\varsigma(h(x,y)) = h(x,y)$, the Hermitian condition is the symmetry, and the four kinds of the diagonal are the classical four kinds of a symmetric bilinear form; the order that the form defines is the order of *Positive Definite Forms and the Order*, and the cone of the positive semi-definite forms is the classical cone of the positive semi-definite symmetric bilinear forms.

*Proof.* With $\varsigma = \mathrm{id}$ the second slot rule is the first and the form is $R$-bilinear; the Hermitian condition $h(y,x) = \varsigma(h(x,y)) = h(x,y)$ is the symmetry; the diagonal is the associated quadratic form $q(x) = h(x,x)$, and its sign is the definiteness of the symmetric form in the sense of *Bilinear Forms*. $\square$

**Remark.** The comparison locates what the twist adds: over the trivial base involution positivity is the positivity of a quadratic form, and the bilinear layer's three kinds of form, of which *Bilinear Forms* treats the symmetric one, are the three fixed points of the dictionary of *The Sesquilinear Form and the Conjugation*. The companion in the bilinear layer, where the conjugation is kept and the form is the one attached to the dagger, is *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint*, whose positive cone is the cone of the elements $x^{\dagger}x$ of a Clifford algebra.

### The Collapse

**Theorem.** Let $\varsigma = \mathrm{id}$ and $* = \mathrm{id}$. Then the form is $h(x,y) = \varphi(yx)$ for a functional $\varphi$, its diagonal is $h(x,x) = \varphi(x^{2})$, and the form is positive semi-definite exactly when $\varphi$ is nonnegative on the squares of the algebra; the algebraic cone of the Hermitian squares is then the cone of the squares $x^{2}$, and the collapse is the one of the bilinear degree-2 form layer.

*Proof.* With the two involutions trivial the compatible forms are $\varphi(yx)$ by the correspondence of *The Sesquilinear Form and the Conjugation*, the diagonal is $\varphi(x^{2})$, and the cone of the Hermitian squares is the semiring of the sums of squares. $\square$

**Remark.** The collapse shows that positivity is not an artefact of the twist: over the trivial involution it is the classical positivity of a quadratic form, and the sequence of reductions — the sesquilinear form to its functional, the functional to its values on the cone of the squares, the cone to the cone of the quadratic form — is the same sequence read without the conjugation. What the twist changes is the cone: $\sum x_i^{*}x_i$ with $*$ nontrivial is a cone of a different shape from $\sum x_i^{2}$, and the properness of the two cones is decided by different criteria, as the matrix model and the non-proper examples of *Hermitian Squares and the Algebraic Positive Cone* show.

## Examples

### The Matrix Algebra

**Example (the matrix algebra, verdict: positive definite).** Let $A = M_n(\mathbb{C})$ with the conjugate transpose and the form $h(X,Y) = \operatorname{tr}(XY^{*})$, and let $R = \mathbb{C}$ with the conjugation, so that $R^{\varsigma} = \mathbb{R}$. Then

$$
h(X,X) = \operatorname{tr}(XX^{*}) = \sum_{i,j} \lvert X_{ij}\rvert^{2} ,
$$

a sum of squares of moduli, hence $\geq 0$, and it is $0$ only for $X = 0$; the form is positive definite and, by the theorem, the algebraic cone of the matrix algebra is proper. The verdict: the model of the layer is the model of the definite case, and the functional is the trace, central and strictly positive on the nonzero cone of the Hermitian squares.

### The Field and the Biquaternion Algebra

**Example (the field).** Let $A = \mathbb{C}$ with the conjugation and $h(z,w) = z\varsigma(w) = z\bar w$. Then $h(z,z) = \lvert z\rvert^{2} \geq 0$ with equality only at $z = 0$, so the form is positive definite; the same computation on a field with a nontrivial involution gives $\varsigma(x)x$, a product of an element with its conjugate, nonnegative for an order-preserving involution that is positive in the sense of *Unitary Geometry over a Field with Involution*.

**Example (the biquaternion algebra).** Let $A = \mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with the scalar part and the form $h(P,Q) = \mathrm{Sc}(Q^{*}P)$. Then

$$
h(Q,Q) = \mathrm{Sc}(Q^{*}Q) = \sum_{\mu=0}^{3} \lvert Q_{\mu}\rvert^{2} ,
$$

the sum of the modulus squares of the coordinates, positive definite by *The Hermitian Form on the Biquaternion Algebra*; the verdict is the positive definiteness of the form $\mathrm{Sc}(Q^{*}Q')$ of *The Form on the Biquaternion Algebra as a Sesquilinear Form*, and its companion $\mathrm{Sc}(\bar QQ') = \sum_{\mu}\varepsilon_{\mu}\bar{Q_{\mu}}Q'_{\mu}$ is indefinite, of signature $(2,6)$ over $\mathbb{R}$, the quaternion sesquilinear form of *The Four Pairings of the Biquaternion Algebra*; here $\varepsilon=(1,-1,-1,-1)$ is the sign vector of the coefficient basis, so that the sum is the four terms $\bar Q_0Q'_0-\bar Q_1Q'_1-\bar Q_2Q'_2-\bar Q_3Q'_3$.

### The Split Algebra

**Example (the split algebra, verdict: not positive semi-definite).** Let $A = R \times R$ with the componentwise product, the swap involution and $\varsigma = \mathrm{id}$ on the ordered ring $R$, and let $\varphi(u,v) = u + v$. The diagonal is

$$
h\bigl((a,b),(a,b)\bigr) = \varphi\bigl((ab,ab)\bigr) = 2ab ,
$$

which is negative for $a = 1$, $b = -1$, so the form is not positive semi-definite, and the same diagonal vanishes on the two coordinate axes, so even the null set is not the radical. The verdict: positivity is not automatic, and the split algebra of *Hermitian Forms on a Sesqualgebra*, §*The Field and the Split Algebra*, whose form is nondegenerate, is the witness that nondegeneracy neither gives nor is given by positivity.

### The Indefinite Form and the Positive Set

**Example (a nondegenerate indefinite form, verdict: the null set is larger than the radical and the positive set is not a cone).** Let $A = R^{2}$ with the componentwise product, the identity involution and $\varsigma = \mathrm{id}$, and let

$$
h(x,y) = x_{1}y_{1} - x_{2}y_{2} .
$$

The form is symmetric bilinear and compatible: $h(xy,z) = x_{1}y_{1}z_{1} - x_{2}y_{2}z_{2} = h(y,xz)$. Its radical vanishes, since $x_{1}y_{1} = x_{2}y_{2}$ for all $y$ forces $x = 0$, while its null set is the two lines $x_{1} = \pm x_{2}$, nonzero. Its positive set is the double cone $\lvert x_{1}\rvert \geq \lvert x_{2}\rvert$, which is not closed under addition, since $(2,1) + (-2,1) = (0,2)$ has $h = -4 < 0$. And the tolerance is not transitive: $(2,1) \succeq (0,0)$ and $(0,0) \succeq (2,-1)$, because $h((2,1),(2,1)) = 3 = h((-2,1),(-2,1))$, while $(2,1) \not\succeq (2,-1)$, because $h((0,2),(0,2)) = -4 < 0$. The verdict: for an indefinite form the null set contains the radical strictly, the positive set is a genuine subset of $A$, and the tolerance is symmetric, not transitive and not an order; the classification of these forms by inertia and signature is *The Indefinite Case and the Signature*.

### The Characteristic-Two Case

**Example (the base of characteristic two, verdict: no positivity).** An ordered ring has characteristic zero: the unit is positive and every multiple $n\cdot1$ is a sum of positive elements, hence positive, so $n\cdot1 \neq 0$. A base of characteristic two such as $\mathbb{F}_{2}$ therefore admits no order, the condition $h(x,x) \geq 0$ has no content there, and the collapse of the scalar dictionary at $\varsigma = \mathrm{id}$ in characteristic two, recorded in *The Sesquilinear Form and the Conjugation*, §*The Failure When $2$ Is Not Invertible*, carries no sign. The verdict: positivity is a phenomenon of the base of characteristic zero, and the model is the conjugation of $\mathbb{C}$ with $R^{\varsigma} = \mathbb{R}$; the algebraic collapse of the two orientations at the identity datum is a collapse of the forms and not of their signs.

## Summary

A Hermitian form on a sesqualgebra is **positive semi-definite** when its diagonal is nonnegative and **positive definite** when the diagonal is strictly positive away from zero, with the negative and the indefinite cases read by the same rule; the diagonal lies in the fixed ring $R^{\varsigma}$ and scales by the square, $h(\lambda x,\lambda x) = \lambda^{2}h(x,x)$. The **positive semi-definite forms form a cone** in the module of the Hermitian forms, closed under addition and under the nonnegative fixed scalars, and this is the cone condition of the layer. The **tolerance** $x \succeq y$ defined by $h(x-y,x-y) \geq 0$ is reflexive, symmetric and translation invariant, and it is transitive exactly for the semi-definite forms; it is not an order, the genuine order of the layer being on the Hermitian elements through the cone of the Hermitian squares and the positive functionals. The positive set $P(h) = \{x : h(x,x)\geq0\}$ satisfies $P(h)\cap(-P(h)) = N(h)$, is stable under the fixed scalars, and is all of $A$ exactly in the positive semi-definite case, while it is not closed under addition for an indefinite form. The **null set** $N(h)$ contains the radical always and equals it for a positive semi-definite form, by the Cauchy–Schwarz inequality, so for such a form the radical is the null set and it is a subspace; the form descends to the quotient $A/A^{\perp}$, which is the largest quotient on which the form is positive definite.

Positivity of the form **is** positivity of the functional on the algebraic cone: for $h_{\varphi}(x,y) = \varphi(y^{*}x)$ the diagonal is $h_{\varphi}(x,x) = \varphi(x^{*}x)$, so $h_{\varphi}$ is positive semi-definite exactly when $\varphi$ is nonnegative on the cone $C(A)$ of the Hermitian squares and positive definite exactly when $\varphi$ is strictly positive on its nonzero elements. A positive definite form is therefore a **certificate of properness** for the algebraic cone, by the criterion of *Hermitian Squares and the Algebraic Positive Cone*; the converse is not claimed. At $\varsigma = \mathrm{id}$ the form is symmetric bilinear, the diagonal is a quadratic form and the four kinds are the classical ones, the companion in the bilinear layer being *Positivity and the Hermitian Cone of a Hilbert Algebra with Hermitian Adjoint*; at $* = \mathrm{id}$ as well the form is $\varphi(yx)$, its diagonal is $\varphi(x^{2})$, and the cone of the squares is the cone of the quadratic form. The model is the matrix algebra with $\operatorname{tr}(XY^{*})$, positive definite, with the biquaternion form $\mathrm{Sc}(Q^{*}Q')$ and the field form $z\bar w$ as the other definite cases; the split algebra is not positive semi-definite, and the form $x_{1}y_{1} - x_{2}y_{2}$ on $R^{2}$ is the nondegenerate indefinite example where the null set is larger than the radical, the positive set is not a cone, and the tolerance is not transitive.

## Summary of Notation

| symbol | meaning |
|---|---|
| $h(x,x) \geq 0$ | the positive semi-definite condition, the diagonal in the ordered fixed ring |
| $h(x,x) > 0$ for $x \neq 0$ | the positive definite condition |
| $h(\lambda x,\lambda x) = \lambda^{2}h(x,x)$ | the scaling of the diagonal by the fixed scalars |
| $x \succeq y \iff h(x-y,x-y) \geq 0$ | the tolerance defined by the form, reflexive, symmetric and translation invariant, not an order |
| $P(h) = \{x : h(x,x) \geq 0\}$ | the positive set, $P(h) = A$ exactly in the semi-definite case |
| $N(h) = \{x : h(x,x) = 0\}$ | the null set, equal to the radical when the form is positive semi-definite |
| $A^{\perp}$ | the radical of the entry, contained in the null set always |
| $A/A^{\perp}$ | the quotient of the module on which the descended form is positive definite |
| $h_{\varphi}(x,y) = \varphi(y^{*}x)$ | the form of the functional, with diagonal $\varphi(x^{*}x)$ |
| $C(A)$ | the algebraic cone of the Hermitian squares of *Hermitian Squares and the Algebraic Positive Cone* |
| $\varsigma = \mathrm{id}$ | the symmetric bilinear case, the quadratic form and the classical positivity |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, volume 1 (Academic Press, 1983), for the positive functionals, the Cauchy–Schwarz inequality and the order they define.
- Jacques Dixmier, *Les $C^{*}$-algèbres et leurs représentations* (Gauthier-Villars, 1964), for the cone of the positive functionals and the construction of the representation from a positive form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the Hermitian forms and the order of the base that their positivity requires.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the sign of a Hermitian form, the positive definite forms and the induced order.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for the positive cone of an involutive algebra and the order it defines.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for the positive functionals of an involutive ring and the order of the self-adjoint part.
