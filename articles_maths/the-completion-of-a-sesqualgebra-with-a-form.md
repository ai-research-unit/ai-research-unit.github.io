# __The Completion of a Sesqualgebra with a Form__

## Introduction

A sesqualgebra with a form is a topological sesqualgebra carrying a continuous Hermitian form tied to the product, and when the form is positive definite its diagonal is a norm, $\lVert x\rVert = h(x,x)^{1/2}$, by *The Norm Defined by a Form*. That article assumes the object complete, and *The Completion of a Sesqualgebra* removes the assumption for the layer without a form: it completes the normed object and extends the product, the twisted scalar action and the involution. Neither names a form. This article supplies the missing case. It takes a normed sesqualgebra with a positive definite form, completes it, and shows that the form itself extends — so that the completed object is again a sesqualgebra with a form over the same datum, the form of the completion is definite with the same norm, and the completion is the universal complete object in which the given one sits densely and isometrically.

Three facts organise the article. The **form extends** because it is a bounded pairing: the Cauchy–Schwarz inequality of *The Norm Defined by a Form* gives $\lvert h(x,y)\rvert \leq \lVert x\rVert\lVert y\rVert$, so $h$ is uniformly continuous on the bounded sets and has a unique continuous extension to the completion; the extension is biadditive, Hermitian and definite, and it computes the norm of the completion, $\widehat{h}(x,x)=\lVert x\rVert^{2}$. The **product and the involution extend** by the argument of *The Completion of a Sesqualgebra*: the product because it is jointly continuous from submultiplicativity, the involution because the $\mathrm{C}^{*}$-condition $\lVert x^{*}x\rVert=\lVert x\rVert^{2}$ makes it isometric and hence uniformly continuous; the **compatibility** $h(xy,z)=h(y,x^{*}z)$ of *Topological Sesqualgebras with a Form*, being an identity between continuous functions on the triple product, then extends with them. And the **completion is universal**: every isometric morphism of sesqualgebras with a form into a complete object factors uniquely through the canonical dense embedding, so the completion is a functor and it is idempotent.

The article defines the normed and the Banach objects, proves the boundedness and the extension of the form, of the product and of the involution, shows that the extended form is compatible and definite, states the universal property, treats the semi-definite case in which the completion kills the radical, and works the examples, the finite-rank operators being the genuinely incomplete one. The norm and the positivity of the form are *The Norm Defined by a Form*; the layer without a form is *The Completion of a Sesqualgebra*; the compatibility is *Topological Sesqualgebras with a Form*; the definite completed case of the bilinear layer is *The Completion of a Hilbert Algebra*. Throughout, the base $(R,\varsigma)$ is one of the two classical kinds of *The Norm Defined by a Form* — $R = k$ an ordered field with $\varsigma = \mathrm{id}$ in which every nonnegative element is a square, or $R = k(i)$ with $\varsigma$ the conjugation — with fixed field $k = R^{\varsigma}$ and modulus $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$; for the completion $R$ is assumed complete, so the models are $R = \mathbb{R}$ with $\varsigma = \mathrm{id}$ and $R = \mathbb{C}$ with the conjugation. The algebra $A$ is an associative normed $R$-algebra with an isometric $\varsigma$-semilinear involution $*$, and $h : A \times A \to R$ is a continuous Hermitian form compatible with the product, linear in the first slot and $\varsigma$-semilinear in the second.

## The Normed Object

### The Definition

**Definition.** A **normed sesqualgebra with a form** over $(R,\varsigma)$ is a normed $R$-space $A$ with an associative product, a $\varsigma$-semilinear involution $*$, and a Hermitian form $h : A \times A \to R$, linear in the first slot and $\varsigma$-semilinear in the second, such that

$$
h(xy, z) = h(y, x^{*}z) \qquad \text{for all } x, y, z \in A ,
$$

with the norm read from the form, $\lVert x\rVert = h(x,x)^{1/2}$, and subject to the two axioms

$$
\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert , \qquad \lVert x^{*}x\rVert = \lVert x\rVert^{2} .
$$

A **Banach sesqualgebra with a form** is one that is complete for this norm, and the sesqualgebra of the object is the derived operation $x \star y = xy^{*}$.

The positivity of the form makes the diagonal non-negative and in the fixed field $k = R^{\varsigma}$, the first axiom is submultiplicativity of the norm, and the second is the $\mathrm{C}^{*}$-condition whose first consequence is the isometry of the involution, $\lVert x^{*}\rVert = \lVert x\rVert$, by *The Norm Defined by a Form*, §*The $\mathrm{C}^{*}$-Condition*. The three demands are exactly those of that article with completeness deleted, and the compatibility is the identity of *Topological Sesqualgebras with a Form*, §*The Identity and Its Equivalent*.

**Proposition (what the completion has to preserve).** The compatibility is equivalently $h(x, yz) = h(y^{*}x, z)$, so the two forms $h(xy,z)$ and $h(y,x^{*}z)$ are the two readings of one identity; the radical of $h$ is a left ideal; and the derived product is compatible with the form in the ternary sense $h(xy^{*}z, w) = h(z, yx^{*}w)$.

*Proof.* These are the three theorems of *Topological Sesqualgebras with a Form*, §*The Identity and Its Equivalent* and §*The Radical Is an Ideal*, stated for a normed object; the proofs use only the product, the involution and the form, hence are available before the completion. $\square$

## The Extension of the Form

### Boundedness

**Theorem (the form is bounded).** For all $x, y \in A$,

$$
\lvert h(x,y)\rvert \leq \lVert x\rVert\,\lVert y\rVert ,
$$

so $h$ is continuous with constant one for the product topology of the norms, and it is uniformly continuous on every bounded set.

*Proof.* This is the Cauchy–Schwarz inequality of *The Norm Defined by a Form*, §*The Cauchy–Schwarz Inequality*, proved from the translated diagonal $h(x-\mu y, x-\mu y) \geq 0$ at $\mu = h(x,y)/h(y,y)$. The bound is the statement that the pairing is bounded with constant one, hence continuous; a bounded biadditive map is uniformly continuous on bounded sets because the estimate is uniform in the arguments. $\square$

**Remark (the bound is sharp on the model).** The estimate is attained: on the matrices of the example below the identity matrix with itself has $\lvert h(1,1)\rvert = \lVert 1\rVert^{2}$, and more generally $y = x$ gives equality when $h(x,x) = \lVert x\rVert^{2}$ is real, which it is, the diagonal lying in $k$.

### The Extension

**Theorem (the form extends uniquely).** Let $A$ be a normed sesqualgebra with a form and let $\widehat{A}$ be its completion, with $\iota : A \to \widehat{A}$ the canonical isometric embedding of dense image. Then there is exactly one continuous map $\widehat{h} : \widehat{A} \times \widehat{A} \to R$ with $\widehat{h}(\iota x, \iota y) = h(x,y)$, and it is a Hermitian form, linear in the first slot and $\varsigma$-semilinear in the second, with

$$
\widehat{h}(x,x) = \lVert x\rVert^{2} \geq 0 , \qquad \lvert\widehat{h}(x,y)\rvert \leq \lVert x\rVert\lVert y\rVert ,
$$

so $\widehat{h}$ is positive definite, and its radical is zero.

*Proof.* By the boundedness theorem $h$ is uniformly continuous on the products of bounded sets, and every element of $\widehat{A}$ is the limit of a bounded sequence from $\iota(A)$; for sequences $x_{n}\to x$, $y_{n}\to y$ the values $h(x_{n},y_{n})$ form a Cauchy sequence in the complete field $R$, because $\lvert h(x_{n},y_{n})-h(x_{m},y_{m})\rvert \leq \lVert x_{n}-x_{m}\rVert\lVert y_{n}\rVert+\lVert x_{m}\rVert\lVert y_{n}-y_{m}\rVert$, and the limit is independent of the chosen sequences by the same estimate; that limit is the definition of $\widehat{h}(x,y)$. The extension is biadditive because addition and the scalar rules are continuous on the completion and the two sides agree on the dense set $\iota(A)\times\iota(A)$; the Hermitian property, the slot rules and the bound are identities of continuous functions verified on that set. The diagonal is $\widehat{h}(x,x) = \lim_n h(x_n,x_n) = \lim_n\lVert x_n\rVert^{2} = \lVert x\rVert^{2}$ for a sequence $x_n \to x$, which is non-negative, and vanishes exactly at $x = 0$; the bound is the Cauchy–Schwarz inequality applied in the limit. $\square$

**Remark (why definiteness survives).** The important point is that the extension is *definite*, so the completed object is again an object of the layer and not merely a form-carrying space: the radical of $\widehat{h}$ is the closure in $\widehat{A}$ of the radical of $h$, and when $h$ is definite on the dense subspace the closure is zero. Definitude is thus the property that the completion does not degrade, which is why the standing hypothesis of the layer is a positive definite form and not a semi-definite one.

## The Extension of the Product and the Involution

### The Product

**Theorem (the product extends).** The product of $A$ extends uniquely to a jointly continuous bilinear map $\widehat{A} \times \widehat{A} \to \widehat{A}$, which is

$$
xy = \lim_n x_n y_n \qquad \text{for } x_n \to x, \ y_n \to y ,
$$

associative, submultiplicative, and with the same unit when $A$ has one.

*Proof.* This is the theorem of *The Completion of a Sesqualgebra*, §*The Completion*: submultiplicativity makes the product jointly continuous, so it is uniformly continuous on the products of bounded sets; the extension exists by density and completeness of $\widehat{A}$, associativity and submultiplicativity are identities on a dense set, and the unit is a fixed point of the formula. $\square$

**Remark (the twisted action).** The twisted scalar action $\lambda \cdot x = \varsigma(\lambda)x$ extends by the same continuity, because the multiplication by a fixed scalar is a homeomorphism of the completion; the conjugate module of the completion is the completion of the conjugate module, $\widehat{A^{\varsigma}} = \widehat{A}^{\varsigma}$, and the derived operation extends to $x \star y = xy^{*}$ once the involution does.

### The Involution

**Theorem (the involution extends).** Under the $\mathrm{C}^{*}$-condition the involution is isometric, $\lVert x^{*}\rVert = \lVert x\rVert$, hence uniformly continuous, and it extends uniquely to an isometric $\varsigma$-semilinear involution $\widehat{*}$ of $\widehat{A}$ with $\widehat{*}^{2} = \mathrm{id}$ and

$$
(xy)^{*} = y^{*}x^{*} \qquad \text{for all } x, y \in \widehat{A} .
$$

*Proof.* The isometry is the theorem of *The Norm Defined by a Form*, §*The $\mathrm{C}^{*}$-Condition*, and an isometry of a normed space into a complete one extends uniquely by uniform continuity. The involution of order two and the anti-multiplicativity are identities of continuous maps agreeing on the dense set $\iota(A)$, hence everywhere. $\square$

**Remark (what is needed and what is not).** The $\mathrm{C}^{*}$-condition is used only through the isometry of the involution; if the involution is continuous with a bound $\lVert x^{*}\rVert \leq c\lVert x\rVert$ it extends as well, and the extension is continuous but need not be isometric. Without any continuity of the involution the extension fails to be a map of the completion, exactly as in the layer without a form, so the continuity of $*$ is part of the hypothesis of the completed object.

### The Compatibility of the Extension

**Theorem (the compatibility extends).** The forms and the operations of the completion satisfy

$$
\widehat{h}(xy, z) = \widehat{h}(y, x^{*}z) \qquad \text{for all } x, y, z \in \widehat{A} ,
$$

so that $(\widehat{A}, \widehat{h})$ is a Banach sesqualgebra with a form over $(R,\varsigma)$, with the derived operation $x \star y = xy^{*}$ and the same involution.

*Proof.* Both sides are continuous functions of the triple $(x,y,z)$ on $\widehat{A}^{3}$, and they agree on the dense subset $\iota(A)^{3}$ by the compatibility of $h$ on $A$. Two continuous maps that agree on a dense set are equal. $\square$

## The Completed Object and Its Universal Property

### The Completed Object

**Theorem (the completion is an object of the layer).** Let $A$ be a normed sesqualgebra with a form. Then $\widehat{A}$, with the extended product, the extended involution and the extended form, is a Banach sesqualgebra with a form; the canonical map $\iota$ is an isometric morphism, injective, with dense image; $\iota$ preserves the product, the involution and the form; and the norm of the completion is the norm defined by its form.

*Proof.* The extensions are the three theorems above; each structure is preserved by construction, and the identity $\widehat{h}(x,x) = \lVert x\rVert^{2}$ of the extension theorem says that the norm of the completion is the norm of its form. Injectivity is the definiteness of $h$; density is the definition of a completion. $\square$

### The Universal Property

**Definition.** A **morphism of sesqualgebras with a form** is a continuous $R$-linear map $f : A \to B$ between such objects that preserves the product, the involution and the form,

$$
f(xy) = f(x)f(y), \qquad f(x^{*}) = f(x)^{*}, \qquad h_{B}(f x, f y) = h_{A}(x,y) ,
$$

and it is **isometric** when moreover $\lVert f x\rVert = \lVert x\rVert$ for every $x$.

**Theorem (the universal property).** Let $A$ be a normed sesqualgebra with a form, let $B$ be a Banach one, and let $f : A \to B$ be an isometric morphism. Then there is exactly one continuous morphism $\widehat{f} : \widehat{A} \to B$ with $\widehat{f}\circ\iota = f$, and it is isometric.

*Proof.* Uniqueness and existence of the continuous linear extension are density and completeness, as in *The Completion of a Sesqualgebra*, §*The Universal Property*; the preservation of the product, the involution and the form is the equality of continuous maps agreeing on the dense set $\iota(A)$. The isometry of $\widehat{f}$ follows from the isometry of $f$ and the identity $\lVert x\rVert^{2} = \widehat{h}(x,x) = h_{B}(\widehat{f}x, \widehat{f}x)$ in the limit. $\square$

**Corollary (the completion is a functor and is idempotent).** The assignment $A \mapsto \widehat{A}$ is a functor on the normed sesqualgebras with a form, valued in the Banach ones and left adjoint to the inclusion; the canonical map $\iota : A \to \widehat{A}$ is the unit. It is idempotent, $\widehat{\widehat{A}} \cong \widehat{A}$ through $\iota$.

*Proof.* The universal property is the statement of the adjunction; for the idempotence, $\widehat{A}$ is complete, so $\iota_{\widehat{A}} : \widehat{A} \to \widehat{\widehat{A}}$ is an isometric isomorphism by the uniqueness clause. $\square$

## The Semi-Definite Case and the Radical

**Proposition (a semi-definite form is a seminorm).** Let $h$ be positive semi-definite and compatible, and put $\lVert x\rVert = h(x,x)^{1/2}$. Then $\lVert\cdot\rVert$ is a seminorm, the Cauchy–Schwarz inequality $\lvert h(x,y)\rvert \leq \lVert x\rVert\lVert y\rVert$ holds, and the null set $N = \{x : \lVert x\rVert = 0\}$ is the radical of $h$, a closed left ideal equal to its own image under the involution when $h$ is also right-definite.

*Proof.* Positive semi-definiteness gives the seminorm axioms by the same diagonal argument as the definite case; the Cauchy–Schwarz inequality is unchanged, with the dependency case included; its equality analysis gives $N = \{x : h(x,y) = 0 \ \forall y\}$, which is the radical, and the radical is a left ideal by *Topological Sesqualgebras with a Form*, §*The Radical Is an Ideal*. $\square$

**Theorem (the completion kills the radical).** Let $h$ be positive semi-definite and compatible, let $\overline{N}$ be the closure of its radical in the completion of the seminormed space, and let $\widehat{A}$ be the completion. Then the extended form $\widehat{h}$ is positive semi-definite with radical $\overline{N}$, and the completion of the quotient $A/N$ is canonically isometric to the quotient $\widehat{A}/\overline{N}$, on which the form is definite.

*Proof.* The extension exists by boundedness; its diagonal is $\lVert x\rVert^{2}$, so its radical is the set of classes of seminorm zero, which is $\overline{N}$. The quotient of a normed space by a closed subspace is a normed space whose completion is the quotient of the completions, and on it the seminorm is a norm; the algebraic operations descend because $N$ is an ideal. $\square$

**Remark (why the layer asks for definiteness).** The theorem is the precise sense in which the standing hypothesis of the layer is definiteness and not mere semi-definiteness: a semi-definite object completes to the definite object $A/\overline{N}$, so the form of the layer is recovered by the completion exactly when the object had no radical, and the examples of *Topological Sesqualgebras with a Form* in which the radical is a proper left ideal are precisely those that the completion quotients away.

## Worked Cases

### The Finite-Rank Operators

**Example (the Hilbert–Schmidt completion, verdict: the genuinely incomplete model).** Let $H$ be a complex Hilbert space, let $A = F(H)$ be the finite-rank operators with the product of composition, the involution the Hilbert adjoint, and the form

$$
h(S,T) = \operatorname{tr}(ST^{*}) ,
$$

the Hilbert–Schmidt pairing, with the norm $\lVert S\rVert_{HS} = \operatorname{tr}(SS^{*})^{1/2}$. Then $A$ satisfies every axiom of a normed sesqualgebra with a form except the $\mathrm{C}^{*}$-condition: the form is positive definite and the Hilbert–Schmidt norm is submultiplicative, because $\lVert ST^{*}\rVert_{HS} \leq \lVert S\rVert_{op}\lVert T\rVert_{HS} \leq \lVert S\rVert_{HS}\lVert T\rVert_{HS}$ with $\lVert S\rVert_{op} \leq \lVert S\rVert_{HS}$; the involution is isometric for the Hilbert–Schmidt norm, $\lVert S^{*}\rVert_{HS} = \lVert S\rVert_{HS}$; and the compatibility holds by the cyclicity of the trace,

$$
h(SR, T) = \operatorname{tr}(SRT^{*}) = \operatorname{tr}(R(S^{*}T)^{*}) = h(R, S^{*}T) .
$$

The $\mathrm{C}^{*}$-condition fails as soon as $\dim H \geq 2$: at an isometry $S$ of rank two one has $\lVert S^{*}S\rVert_{HS} = \sqrt{2}$ while $\lVert S\rVert_{HS}^{2} = 2$, the computation already met at the matrix trace form. The example is therefore the one in which the $\mathrm{C}^{*}$-condition can be dropped, the isometry of the involution being all that the extension of $*$ needs by §*The Algebra Involution*. The object is **not complete**: the finite-rank operators are dense in the Hilbert–Schmidt class $L^{2}(H)$, which is a Hilbert space, and the limit of finite-rank operators is a Hilbert–Schmidt operator. The completion is $L^{2}(H)$ with the Hilbert–Schmidt norm, the extended product is the composition of Hilbert–Schmidt operators, the class $L^{2}(H)$ being closed under it because $\lVert ST\rVert_{HS} \leq \lVert S\rVert_{HS}\lVert T\rVert_{HS}$, the extended involution is the adjoint, and the extended form is the Hilbert–Schmidt inner product. The example is the model in which the completion is a genuine enlargement, and it is the completion statement of *Topological Sesqualgebras with a Form* read for a definite form that is not the operator norm.

### The Field and the Matrices

**Example (the field and the matrices, verdict: already complete).** Let $A = \mathbb{C}$ with the form $h(z,w) = z\overline{w}$, or $A = M_{n}(\mathbb{C})$ with the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$ and the Frobenius norm, the models of *The Norm Defined by a Form*. Both are complete, because the field is complete and the matrix algebra is finite dimensional; the completion changes nothing and the universal property is read with $\widehat{A} = A$ and $\iota$ the identity. The example is the trivial completion, and it shows that the completion is idempotent on the standard models: the objects of the layer that are finite dimensional over a complete field are already Banach.

### The Collapse at the Trivial Involution

**Theorem (the collapse of the completion).** Let $\varsigma = \mathrm{id}$. Then the form is symmetric and $R$-bilinear, the completed object is a normed and complete $R$-algebra with a symmetric definite form invariant in the sense $h(xy,z) = h(y,xz)$, and when $* = \mathrm{id}$ the object is the completion of a normed algebra with a self-adjoint left multiplication and a symmetric definite form — the object of *The Completion of a Hilbert Algebra* in the tracial case, where the involution is isometric, and the bilinear counterpart of the completion otherwise.

*Proof.* At $\varsigma = \mathrm{id}$ the semilinearity of the involution and of the second slot are linearity, the compatibility of *Topological Sesqualgebras with a Form*, §*The Collapse at the Trivial Involution* gives the invariance $h(xy,z)=h(y,xz)$, and the completion statements are the ones above read at the trivial involution. The identification with the Hilbert-algebra completion is the collapse theorem of *The Norm Defined by a Form*, §*The Collapse at the Trivial Involution*. $\square$

**Remark.** The sesquilinear content of the article is exactly the extension of the twisted second slot and of the $\varsigma$-semilinear involution: at $\varsigma = \mathrm{id}$ the extension is the classical completion of a normed space with two structure maps, and the only trace of the twist is the modulus $\lvert\lambda\rvert = (\lambda\varsigma(\lambda))^{1/2}$ of the norm, which at the collapse is the absolute value of the ordered field.

## Summary

A **normed sesqualgebra with a form** is a normed sesqualgebra whose norm is read from a positive definite Hermitian form, $\lVert x\rVert = h(x,x)^{1/2}$, with submultiplicativity and the $\mathrm{C}^{*}$-condition; its completion $\widehat{A}$ is a **Banach sesqualgebra with a form** over the same datum. The **form extends** because it is a bounded pairing, $\lvert h(x,y)\rvert \leq \lVert x\rVert\lVert y\rVert$ by Cauchy–Schwarz, and the extension is definite by the identity $\widehat{h}(x,x) = \lVert x\rVert^{2}$; the **product extends** by the joint continuity that submultiplicativity supplies, and the **involution extends** because the $\mathrm{C}^{*}$-condition makes it isometric; the **compatibility extends** with them because it is an identity between continuous functions verified on the dense subspace. The completion is the **universal** complete object: every isometric morphism of sesqualgebras with a form into a Banach one factors uniquely through the dense embedding, so the assignment is a functor and is idempotent. A **semi-definite** form is a seminorm, and the completion kills its radical, so the completed object carries the definite form of the quotient; definiteness is exactly the hypothesis under which the layer is stable under completion. The worked cases are the **finite-rank operators**, whose completion is the Hilbert–Schmidt class, the **field and the matrices**, which are already complete, and the **collapse** at $\varsigma = \mathrm{id}$, where the object is the completion of a normed algebra with a symmetric definite form.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\lVert x\rVert = h(x,x)^{1/2}$ | the norm defined by the positive definite form |
| $\lVert xy\rVert \leq \lVert x\rVert\lVert y\rVert$ | submultiplicativity, the axiom making the norm an algebra norm |
| $\lVert x^{*}x\rVert = \lVert x\rVert^{2}$ | the $\mathrm{C}^{*}$-condition, giving the isometric involution |
| $\iota : A \to \widehat{A}$ | the canonical isometric embedding of dense image |
| $\widehat{A}$, $\widehat{h}$ | the completion and the extended form |
| $\widehat{h}(x,x) = \lVert x\rVert^{2}$ | definiteness of the extended form |
| $\lvert h(x,y)\rvert \leq \lVert x\rVert\lVert y\rVert$ | boundedness, the source of uniform continuity |
| $xy = \lim_n x_n y_n$ | the extended product |
| $(xy)^{*} = y^{*}x^{*}$ | the extended involution |
| $\widehat{h}(xy,z) = \widehat{h}(y,x^{*}z)$ | the extended compatibility |
| $\widehat{\widehat{A}} \cong \widehat{A}$ | idempotence of the completion |
| $N = \{x : \lVert x\rVert = 0\}$ | the radical of a semi-definite form, killed by the completion |
| $\operatorname{tr}(ST^{*})$ on $F(H)$ | the Hilbert–Schmidt pairing, completing to $L^{2}(H)$ |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the bounded extension theorem, completions of normed spaces and the Cauchy–Schwarz inequality.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the $\mathrm{C}^{*}$-condition, the isometry of the involution and the operator completions.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the Hilbert–Schmidt class, the finite-rank operators and their completions.
- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the extension of the product and of the involution to the completion of a normed algebra.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for positive definite Hermitian forms, their Gram matrices and the quotient by the radical.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the isometric involutions and the forms of an algebra with involution.
